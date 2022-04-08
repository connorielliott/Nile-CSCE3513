import time
# these are ours
from frontEnd import Hermes
from database import DB
import two_arrays


# --- START ----------------- Variables ------------------ START ---

gameState = 0
gameDuration = 360		# Set game time duration variable

database = DB()

# will hold tuples (number id, string name)
redTeam = []
greenTeam = []

# ---- END ------------------ Variables ------------------- END ----


# --- START ------------ Game Countdown Timer ------------ START ---

def startGame(given_hermes):
	global hermes
	hermes = given_hermes
	
	# open db
	database.openDB()
	
	# send team player information to front-ends
	for player in redTeam:
		name = processPlayer(player)
		if name == False:
			return
		elif (name != ""):
			hermes.inform(["name", "team"], [name, "red"])
	for player in greenTeam:
		name = processPlayer(player)
		if name == False:
			return
		elif name != "":
			hermes.inform(["name", "team"], [name, "green"])

	# Game countdown timer begins here
	gameState = 1
	hermes.updateGameState(gameState)
	hermes.log("Begin game in t-minus")
	for i in range(10, 0, -1):
		hermes.clock(i)
		hermes.log(f"{i} seconds")
		time.sleep(1)
	
	#Starts game
	gameState = 2
	hermes.updateGameState(gameState)
	hermes.log("Starting Game")
	gameLoop()

# ---- END ------------- Game Countdown Timer ------------- END ----


# --- START ----------------- Game Loop ------------------ START ---

def gameLoop():
	# Gametime takes place here
	gameTime = gameDuration
	hermes.clock(gameTime)
	while(gameTime > 0):
		# do things
		# if necessary
		
		# decrement time
		time.sleep(1)
		gameTime = gameTime - 1
		hermes.clock(gameTime)
		
		# time warnings
		if(gameTime == 60):
			# One minute warning
			hermes.log("Warning: 1 minute remaining")
		elif (gameTime <= 0):
			endGame()
		elif(gameTime <= 30):
			# End of game countdown
			if(gameTime == 30):
				hermes.log("Game ending in t-minus")
			hermes.log(f"{gameTime} seconds")

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
			hermes.invalidId(id)
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
	hermes.updateGameState(gameState)
	hermes.log("Game over")
	
	# clear teams
	redTeam = []
	greenTeam = []
	
	# close db
	database.closeDB()

# ---- END --------------- Extra Game Stuff --------------- END ----


# --- START ---------- Receiving from Front-End ---------- START ---

playerList = []

# handle front-end messages
def frontEndHandler(given_hermes, msg):
	# parse message
	fields = two_arrays.two_arrays(msg)[0]
	values = two_arrays.two_arrays(msg)[1]
	
	# interpret messages
	id = -1
	name = ""
	stopIndex = max(len(fields), len(values))
	for i in range(0, stopIndex):
		if i < len(fields):
			field = fields[i]
		else:
			field = ""
		if i < len(values):
			value = values[i]
		else:
			value = ""
	
		# the only possible messages are for player entry and to start the game
		# both of these are only possible when gamestate is 0
		if field == "id":
			id = int(value)
		elif field == "name":
			name = value
		elif field == "team":
			addPlayerToTeam((id, name), value)
			id = -1
			name = ""
		elif field == "gameState" and value == "1":
			startGame(given_hermes)

# ---- END ----------- Receiving from Front-End ----------- END ----


# --- START ----------- Receiving from Traffic ----------- START ---

def trafficHandler(msg):
	# to be implemented
	print("handling traffic dutifully.")
	print(f"message sent from client: {msg}")

# ---- END ------------ Receiving from Traffic ------------ END ----


# --- START --------------- Main Function ---------------- START ---

# hermes is the messenger to the front-end
hermes = Hermes(frontEndHandler)
# IF PYTHON HAD FUCKING FUNCTION HOISTING I WOULD NOT HAVE SPENT 5 HOURS TRYING TO FIX THIS SHITTY CIRCULAR IMPORT PROBLEM

# ---- END ---------------- Main Function ----------------- END ----
