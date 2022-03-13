import time
import server	# this is ours, handles messaging front-end


# --- START --------------- Game Variables --------------- START ---

gameState = 0
gameTime = 360									# Set game time duration variable

# ---- END ---------------- Game Variables ---------------- END ----


# --- START ------------- GUI Message Relay -------------- START ---

# handle messages
def handler(msg):
	# always respond with updated gamestate var in front end
	server.send("gameState:{}".format(gameState))
	
	# interpret messages
	#~you were here
	
	# for i in range(0, max(len(fields), len(values))):
		# field = fields[i]
		# value = values[i]
		# gameState update
		#if field == "gameState" and gameState == 0:
			# start countdown

# must be before all server.send(<str>) usages since this gets the address of the bridge
server.start(handler)

# ---- END -------------- GUI Message Relay --------------- END ----


# --- START ------------ Game Countdown Timer ------------ START ---

# Game countdown timer begins here
server.log("Begin game in t-minus")				#print("Begin game in t-minus")
gameState = 1
for i in range(10, 0, -1):
	server.log(i)								#print(i)
	time.sleep(1)


server.log("Starting Game")						#print("Starting Game")  #Starts game
gameState = 2
# Gametime takes place here


# One minute warning
time.sleep(gameTime - 60)
server.log("Warning: 1 minute remaining")		#print("Warning: 1 minute remaining")
time.sleep(30)
#~time.sleep is blocking, may interfere with game stuffs


# End of game countdown
server.log("Game ending in t-minus")			#print("Game ending in t-minus")
for i in range(30, 0, -1):
	server.log(i)								#print(i)
	time.sleep(1)
server.log("Game over")							#print("Game over")
gameState = 0

# ---- END ------------- Game Countdown Timer ------------- END ----
