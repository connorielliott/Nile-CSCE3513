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


# example using server.send(<str>)
print("starting countup")
for i in range(0, 11):
	time.sleep(1)
	server.send("hello " + str(i))
