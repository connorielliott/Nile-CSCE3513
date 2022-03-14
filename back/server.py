import json
import socket
import _thread			# https://stackoverflow.com/a/64402988


localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
address = None
frontEndHandler = None
networkingHandler = None

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))


# send raw message
def send(message):
	if(address == None): 
		print("! address not defined")
		return
	message = str(message)
	print_msg = "[P->n]\t{}".format(message)
	print(print_msg)
	UDPServerSocket.sendto(str.encode(message), address)

# send information (field:value,field:value,...)
def inform(field_array, value_array):
	stop_index = max(len(field_array), len(value_array))
	message = ""
	for i in range(0, stop_index):
		if i < len(field_array):
			field = field_array[i]
		else:
			field = ""
		if i < len(value_array):
			value = value_array[i]
		else:
			value = ""
		message += "{f}:{v}".format(f=field, v=value)
		if i < stop_index - 1:
			message += ","
	send(message)

# send message to log
def log(message):
	send("log:{}".format(message))

# send number of seconds to be registered in clock
def clock(seconds):
	send("clock:{}".format(seconds))

# send gamestate
def updateGameState(gameState):
	send("gameState:{}".format(gameState))

# invalid id message
def invalidId(id):
	send("invalid:{}".format(id))

# Listen for incoming datagrams
def listen():
	print("entering listening loop...")
	while(True):
		# wait for message
		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
		message = bytesAddressPair[0]
		global address
		address = bytesAddressPair[1]
		
		#~differentiate between front-end messsages and network messages
		# handle front-end messages
		message = str(message)[2:-1]
		print("[n->P]\t{}".format(message))
		frontEndHandler(message)
		
		# handle networking messages
		# networkingHandler(message)


# start function, can pass in handler function from main.py
def start(frontEndHandlerFunction, networkingHandlerFunction):
	global frontEndHandler
	global networkingHandler
	frontEndHandler = frontEndHandlerFunction
	networkingHandler = networkingHandlerFunction
	try:
		print("starting listening thread...")
		listen()
	except Exception as e:
		print("! failed listening thread:")
		print(e)
