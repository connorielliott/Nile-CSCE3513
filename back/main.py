import time
# these are ours
import frontEnd
from database import DB


# --- START --------------- Game Variables --------------- START ---

gameState = 0
gameDuration = 360		# Set game time duration variable

database = DB()

# will hold tuples (number id, string name)
redTeam = []
greenTeam = []

# ---- END ---------------- Game Variables ---------------- END ----


# --- START ------------ Game Countdown Timer ------------ START ---

def startGame():
	# open db
	database.openDB()
	
	# send team player information to front-ends
	for player in redTeam:
		name = processPlayer(player)
		if name == False:
			return
		elif (name != ""):
			frontEnd.inform(["name", "team"], [name, "red"])
	for player in greenTeam:
		name = processPlayer(player)
		if name == False:
			return
		elif name != "":
			frontEnd.inform(["name", "team"], [name, "green"])

	# Game countdown timer begins here
	gameState = 1
	frontEnd.updateGameState(gameState)
	frontEnd.log("Begin game in t-minus")
	for i in range(10, 0, -1):
		frontEnd.clock(i)
		frontEnd.log(f"{i} seconds")
		time.sleep(1)
	
	#Starts game
	gameState = 2
	frontEnd.updateGameState(gameState)
	frontEnd.log("Starting Game")
	gameLoop()

# ---- END ------------- Game Countdown Timer ------------- END ----


# --- START ----------------- Game Loop ------------------ START ---

def gameLoop():
	# Gametime takes place here
	gameTime = gameDuration
	frontEnd.clock(gameTime)
	while(gameTime > 0):
		# do things
		# if necessary
		
		# decrement time
		time.sleep(1)
		gameTime = gameTime - 1
		frontEnd.clock(gameTime)
		
		# time warnings
		if(gameTime == 60):
			# One minute warning
			frontEnd.log("Warning: 1 minute remaining")
		elif (gameTime <= 0):
			endGame()
		elif(gameTime <= 30):
			# End of game countdown
			if(gameTime == 30):
				frontEnd.log("Game ending in t-minus")
			frontEnd.log(f"{gameTime} seconds")

# ---- END ------------------ Game Loop ------------------- END ----


# --- START --------------- Database Stuff --------------- START ---

def playerExists(id):
	# determine if this player exists in the database
	return database.searchID(id)

def addPlayerToDatabase(name):
	# add new entry to database with this name. return id of new entry
	id = database.maxID() + 1
	database.insertPlayer(id,name,0)
	return id

def getPlayerName(id):
	# get player name from id
	return database.retrieveName(id)

def updatePlayerName(id, name):
	# obvious
	database.updateName(id,name)


# ---- END ---------------- Database Stuff ---------------- END ----


# --- START -------------- Extra Game Stuff -------------- START ---

def addPlayerToTeam(player, team):
	if team == "red":
		redTeam.append(player)
	elif team == "green":
		greenTeam.append(player)

def processPlayer(player):
	id = player[0]
	name = player[1]
	if(id == -1):
		if(name != ""):
			# new player
			id = addPlayerToDatabase(name)
			return name
		else:
			return ""
	if(name == ""):
		# retrieve name with id if possible, otherwise do not add this player to the teams
		if(playerExists(id)):
			name = getPlayerName(id)
			return name
		else:
			frontEnd.invalidId(id)
			return False
	else:
		if(playerExists(id)):
			# update entry if possible
			updatePlayerName(id, name)
			return name
		else:
			addPlayerToDatabase(name)
			return name
	return ""

def endGame():
	# end game
	gameState = 0
	frontEnd.updateGameState(gameState)
	frontEnd.log("Game over")
	
	# clear teams
	redTeam = []
	greenTeam = []
	
	# close db
	database.closeDB()

# ---- END --------------- Extra Game Stuff --------------- END ----


# --- START --------------- Main Function ---------------- START ---



# ---- END ---------------- Main Function ----------------- END ----
