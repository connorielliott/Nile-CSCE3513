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
	
	def insertPlayer(self,id,first_name,last_name,codename):
		query =  "INSERT INTO player (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s);"
		data = (id, first_name, last_name, codename)
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
