import time
# these are ours
import server
from database import DB


# --- START --------------- Game Variables --------------- START ---

gameState = 0
gameDuration = 30		# Set game time duration variable

database = DB()

# will hold tuples (number id, string name)
redTeam = []
greenTeam = []

# ---- END ---------------- Game Variables ---------------- END ----


# --- START ------------ Game Countdown Timer ------------ START ---

def startGame():
	global display
	display = server.hermes
	
	# open db
	database.openDB()
	
	# send team player information to front-ends
	for player in redTeam:
		name = processPlayer(player)
		if name == False:
			return
		elif (name != ""):
			display.inform(["name", "team"], [name, "red"])
	for player in greenTeam:
		name = processPlayer(player)
		if name == False:
			return
		elif name != "":
			display.inform(["name", "team"], [name, "green"])

	# Game countdown timer begins here
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
	red_score = 0
	green_score = 0
	i = 0
	while(gameTime > 0):
		# do things
		
		# example display score (team "red" or "green", total for that team points this round)
		if (player_scored == red):
			red_score = update_red_score(red_score)
		elif (player_scored == green):
			green_score = update_green_score(green_score)
		display.score("red", red_score)
		display.score("green", green_score)
		i = i + 3

		# example kill message (killer team "red" or "green", killer name, killed team, killed name)
		if(i % 2 == 0):
			display.kill("red", getPlayerName(1), "green", getPlayerName(3))
		else:
			display.kill("green", getPlayerName(4), "red", getPlayerName(2))
		
		
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

def clearTeams():
	global redTeam
	global greenTeam
	redTeam = []
	greenTeam = []

def update_red_score(red_score):
	return red_score + 1

def update_green_score(green_score):
	return green_score + 1

def addPlayerToTeam(player, team):
	if team == "red":
		redTeam.append(player)
	elif team == "green":
		greenTeam.append(player)

def processPlayer(player):
	[id, name] = player
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
			clearTeams()
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
	gameState = 0
	display.updateGameState(gameState)
	display.log("Game over")
	
	
	# example winning team (message to display at top of screen)
	display.state("GREEN Team wins!")
	
	
	# clear teams
	clearTeams()
	
	# close db
	database.closeDB()

# ---- END --------------- Extra Game Stuff --------------- END ----


# --- START --------------- Main Function ---------------- START ---



# ---- END ---------------- Main Function ----------------- END ----
