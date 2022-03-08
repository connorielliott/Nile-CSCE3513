import json
import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Hello from Python Server"

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

# send message back
def send(address, message):
	print("[P->n]\t", str.encode(message))
	UDPServerSocket.sendto(str.encode(message), address)

# handle messages from bridge
def handle_msg(msg, address):
	# say hello as a response
	send(address, msgFromServer)
	
	# this is an example message thing.
	# could use two arrays or maybe a dictionary which associates messages and functions to run
	if(msg == "john"):
		print("YOU SAID JOHN!!!!")
	
	# if(msg == "kill"):
		# somehow call kill_all() in the launcher script
	

# Listen for incoming datagrams
while(True):
	# wait for message
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	message = str(message)[2:-1]
	address = bytesAddressPair[1]
	clientMsg = "[n->P]\t{}".format(message)
	print(clientMsg)
	
	# handle messages
	handle_msg(str(message), address)
