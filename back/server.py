import json
import socket
from threading import Thread


DEBUG = True

localIP     = "127.0.0.1"
recv_port = 7501
broadcast_port = 7500
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, recv_port))


# for broadcasting messages
def broadcast(message, address):
	UDPServerSocket.sendto(str.encode(message), address)


# --- START ------------ Front-End Messaging ------------- START ---

class Hermes:
	def __init__(self):
		relay_address = None
	
	# set relay_address
	def setRelayAddress(self, address):
		self.relay_address = address
	
	# send raw message
	def send(self, message):
		if(self.relay_address == None): 
			print("! relay address not defined")
			return
		message = str(message)
		if(DEBUG):
			print_msg = "[P->n]\t{}".format(message)
			print(print_msg)
		broadcast(message, self.relay_address)
		
	# send information (field:value,field:value,...)
	def inform(self, field_array, value_array):
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
		self.send(message)

	# send message to display at top of screen
	def state(self, message):
		self.send("state:{}".format(message))
	
	# send number of seconds to be registered in clock
	def clock(self, seconds):
		self.send("clock:{}".format(seconds))

	# send team score
	def score(self, team, skore):
		self.send("score:{s},team:{t}".format(t=team, s=skore))

	# send killer and killed
	def kill(self, killerTeam, killer, killedTeam, killed):
		self.send("killed:{d},killedTeam:{l},killer:{r},killerTeam:{w}".format(d=killed, l=killedTeam, r=killer, w=killerTeam))

	# send message to log
	def log(self, message):
		self.send("log:{}".format(message))

	# send gamestate
	def updateGameState(self, gameState):
		self.send("gameState:{}".format(gameState))

	# invalid id message
	def invalidId(self, id):
		self.send("invalid:{}".format(id))

hermes = Hermes()

# ---- END ------------- Front-End Messaging -------------- END ----


# Listen for incoming datagrams
def listen():
	import messageHandler
	
	print("entering listening loop...")
	while(True):
		# wait for message
		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
		message = bytesAddressPair[0]
		address = bytesAddressPair[1]

		message = str(message)[2:-1]
		
		if('0' <= message[0] and message[0] <= '9'):
			print("integer message")
			messageHandler.traffic(message)
		else:
			hermes.setRelayAddress(address)
			print("string message")
			if(DEBUG): print("[n->P]\t{}".format(message))
			thread = Thread(target=messageHandler.frontEnd, args=(message,))
			thread.start()


# start
try:
	print("starting listening thread...")
	listen()
except Exception as e:
	print("! failed listening thread:")
	print(e)
