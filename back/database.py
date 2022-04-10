import psycopg2
from psycopg2 import Error


class DB:

	def __init__(self):
		self.connection = None
		self.cursor = None
		
	def openDB(self):
		try:
			# Connect to an existing database
			self.connection = psycopg2.connect(user="slczonlmjepvad",
										password="6979ac6767322b212530fba90cb3a15982c0afd1c3f49b556ef6f9d801ee40fe",
										host="ec2-54-224-64-114.compute-1.amazonaws.com",
										port="5432",
										database="d4d8vs7acnm5mj")
			self.cursor = self.connection.cursor()
		except (Exception, Error) as error:
			print("Error while connecting to PostgreSQL", error)
	
	def closeDB(self):
		if (self.connection):
			self.cursor.close()
			self.connection.close()
			print("PostgreSQL connection is closed")
		else:
			print("Open Database first")
	
	def insertPlayer(self,id,codename,score):
		query =  "INSERT INTO player (id, codename, score) VALUES (%s, %s, %s);"
		data = (id,codename, score)
		self.cursor.execute(query, data)
		self.connection.commit()
		
	def searchID(self,id):
		
		query = "select COUNT(id) from player WHERE id =" + str(id) + ";"
		self.cursor.execute(query)
		retrieve = self.cursor.fetchall()
		for row in retrieve:
			if row[0] > 0:
				print("Record exists")
				return True
			else:
				print("Record does not exists")
				return False
	
	def maxID(self):
		query = "SELECT id from player order by id desc limit 1;"
		self.cursor.execute(query)
		retrieve = self.cursor.fetchall()
		for row in retrieve:
			return row[0]
	
	def retrieveName(self,id):
		query = "SELECT codename FROM player where id = " + str(id) + ";"
		self.cursor.execute(query)
		retrieve = self.cursor.fetchall()
		for row in retrieve:
			return row[0]
	
	def updateName(self,id,codename):
		query = "UPDATE player SET codename = \'" + codename + "\' WHERE id = " + str(id) + ";"
		self.cursor.execute(query)
		self.connection.commit()
