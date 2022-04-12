import time
# these are ours
import server
from database import DB


# --- START --------------- Game Variables --------------- START ---

gameState = 0
gameDuration = 360		# Set game time duration variable

database = DB()

# player dictionary has int id for key and (string team, string name) tuple for value
players = {}

redScore = 0
greenScore = 0

# ---- END ---------------- Game Variables ---------------- END ----


# --- START ------------ Game Countdown Timer ------------ START ---

def startGame():
	global display
	display = server.hermes
	
	# open db
	database.openDB()
	
	# send team player information to front-ends
	global players
	for id, player in players.items():
		(team, name) = player
		name = processPlayer(id, name)
		if name == False:
			return
		elif (name != ""):
			display.inform(["name", "team"], [name, team])
			players[id] = (team, name)

	# Game countdown timer begins here
	global gameState
	gameState = 1
	display.updateGameState(gameState)
	display.log("Begin game in t-minus")
	for i in range(10, 0, -1):
		display.clock(i)
		display.log("{} seconds".format(i))
		time.sleep(1)
	
	#Starts game
	gameState = 2
	display.updateGameState(gameState)
	display.log("Starting Game")
	gameLoop()

# ---- END ------------- Game Countdown Timer ------------- END ----


# --- START ----------------- Game Loop ------------------ START ---

def gameLoop():
	# Gametime takes place here
	gameTime = gameDuration
	display.clock(gameTime)
	i = 0
	while(gameTime > 0):
		# decrement time
		time.sleep(1)
		gameTime = gameTime - 1
		display.clock(gameTime)
		
		# time warnings
		if(gameTime == 60):
			# One minute warning
			display.log("Warning: 1 minute remaining")
		elif (gameTime <= 0):
			endGame()
		elif(gameTime <= 30):
			# End of game countdown
			if(gameTime == 30):
				display.log("Game ending in t-minus")
			display.log("{} seconds".format(gameTime))

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

def addPlayerToTeam(id, name, team):
	global players
	players[id] = (team, name)

def incrementScore(team):
	if(team == "red"):
		global redScore
		redScore += 1
	elif(team == "green"):
		global greenScore
		greenScore += 1

def processPlayer(id, name):
	if(id == -1):
		if(name != ""):
			# new player (no id, yes name)
			id = addPlayerToDatabase(name)
			return name
		else:
			# do nothing (no id, no name)
			return ""
	if(name == ""):
		# retrieve name with id if possible, otherwise do not add this player to the teams
		# (yes id, no name)
		if(playerExists(id)):
			name = getPlayerName(id)
			return name
		else:
			display.invalidId(id)
			global players
			players = {}
			return False
	else:
		# (yes id, yes name)
		if(playerExists(id)):
			# update entry if possible
			updatePlayerName(id, name)
			return name
		else:
			id = addPlayerToDatabase(name)
			return name
	return ""

def endGame():
	# end game
	global gameState
	gameState = 0
	display.updateGameState(gameState)
	display.log("Game over")
	
	# display scores one last time
	global redScore
	global greenScore
	display.score("red", redScore)
	display.score("green", greenScore)
	
	# display winning team
	if(redScore == greenScore):
		display.state("You're both garbage!")
	elif(greenScore > redScore):
		display.state("GREEN Team wins!")
	else:
		display.state("RED Team wins!")
	
	# reset score
	redScore = 0
	greenScore = 0
	
	# clear players
	global players
	players = {}
	
	# close db
	database.closeDB()

def getPlayer(id):
	# given id of player, return (team, name) tuple of player from team array
	return players[id]

# ---- END --------------- Extra Game Stuff --------------- END ----
