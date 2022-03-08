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
	
	# if(msg == "kill"):
		# somehow call kill_all() in the launcher script
	

# Listen for incoming datagrams
while(True):
	# wait for message
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	clientMsg = "[n->P]\t{}".format(message)
	print(clientMsg)
	
	# handle messages
	handle_msg(str(message), address)
