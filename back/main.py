import time
# these are ours
import messageHandler
import server


# --- START --------------- Game Variables --------------- START ---

gameState = 0
gameDuration = 360		# Set game time duration variable

# will hold tuples (number id, string name)
redTeam = []
greenTeam = []

# ---- END ---------------- Game Variables ---------------- END ----


# --- START ------------ Game Countdown Timer ------------ START ---

def startGame():
	# send team player information to front-end
	for player in redTeam:
		name = processPlayer(player)
		if(name != ""):
			server.inform(["name", "team"], [name, "red"])
	for player in greenTeam:
		name = processPlayer(player)
		if(name != ""):
			server.inform(["name", "team"], [name, "green"])

	# Game countdown timer begins here
	gameState = 1
	server.updateGameState(gameState)
	server.log("Begin game in t-minus")
	for i in range(10, 0, -1):
		server.clock(i)
		server.log("{} seconds".format(i))
		time.sleep(1)
	
	#Starts game
	gameState = 2
	server.updateGameState(gameState)
	server.log("Starting Game")
	gameLoop()

# ---- END ------------- Game Countdown Timer ------------- END ----


# --- START ----------------- Game Loop ------------------ START ---

#~maybe reorganize this?
def gameLoop():
	# Gametime takes place here
	gameTime = gameDuration
	server.clock(gameTime)
	while(gameTime > 0):
		# do things
		# if necessary
		
		# decrement time
		time.sleep(1)
		gameTime = gameTime - 1
		server.clock(gameTime)
		
		# time warnings
		if(gameTime == 60):
			# One minute warning
			server.log("Warning: 1 minute remaining")
		elif (gameTime <= 0):
			endGame()
		elif(gameTime <= 30):
			# End of game countdown
			if(gameTime == 30):
				server.log("Game ending in t-minus")
			server.log("{} seconds".format(gameTime))


# ---- END ------------------ Game Loop ------------------- END ----


# --- START --------------- Database Stuff --------------- START ---

def playerExists(id):
	# determine if this player exists in the database
	return True

def addPlayerToDatabase(name):
	# add new entry to database with this name. return id of new entry
	id = -1
	print("added name={n} with id={i}".format(n=name, i=id))
	return id

def getPlayerName(id):
	# get player name from id
	return "what"

def updatePlayerName(id, name):
	# obvious
	print("updated id={i} to have name={n}".format(i=id, n=name))

# ---- END ---------------- Database Stuff ---------------- END ----


# --- START -------------- Extra Game Stuff -------------- START ---

def addPlayerToTeam(player, team):
	if team == "red":
		redTeam.append(player)
	elif team == "green":
		greenTeam.append(player)

#~check if this is fine, my brain is starting to hurt
def processPlayer(player):
	id = player[0]
	name = player[1]
	if(id == -1):
		# new player
		id = addPlayerToDatabase(name)
	if(name == ""):
		# retrieve name with id if possible, otherwise do not add this player to the teams
		if(playerExists(id)):
			name = getPlayerName(id)
			if(name != ""):
				# update entry
				updatePlayerName(id, name)
		else:
			server.invalidId(id)
			return ""		
	return name

def endGame():
	# end game
	gameState = 0
	server.updateGameState(gameState)
	server.log("Game over")
	
	# clear teams
	redTeam = []
	greenTeam = []

# ---- END --------------- Extra Game Stuff --------------- END ----


# --- START --------------- Main Function ---------------- START ---

# must be before all server.send(<str>) usages since this gets the address of the bridge
server.start(messageHandler.frontEndHandler, messageHandler.networkingHandler)

# do other things
# if necessary
time.sleep(10)
startGame()

# ---- END ---------------- Main Function ----------------- END ----
