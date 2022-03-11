import time

# this is ours, handles messaging front-end
import server

# handle messages from bridge
def handler(msg):
	# say hello as a response
	server.send("Hello from Python Server")
	
	# example handling message from browser
	#~could use two arrays or maybe a dictionary which associates messages and functions to run
	if(msg == "john"):
		print("YOU SAID JOHN!!!!")
	

# actually start listening server
# pass in handler function which can manage messages received from browser
server.start(handler)



# ----------------------Game Countdown Timer----------------------
gameTime = 70  # Set game time duration variable

# Game countdown timer begins here
print("Begin game in t-minus")
for i in range(10, 0, -1):
    server.send(str(i))                        #print(i)
    time.sleep(1)


server.send(str("Starting Game"))              #print("Starting Game")  #Starts game
gameActive = True
# Gametime takes place here


# One minute warning
time.sleep(gameTime - 60)
server.send("Warning: 1 minute remaining")     #print("Warning: 1 minute remaining")
time.sleep(50)


# End of game countdown
server.send("Game ending in t-minus")          #print("Game ending in t-minus")
for i in range(10, 0, -1):
    server.send(str(i))                        #print(i)
    time.sleep(1)
server.send("Game over")                       #print("Game over")
gameActive = False
#------------------------------------------------------------------
