import json
import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Hello from Python Server"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

# send message back
def send(address, bytesToSend):
	UDPServerSocket.sendto(bytesToSend, address)
	print("[.->n]\t", bytesToSend)

# Listen for incoming datagrams
while(True):
	# wait for message
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	clientMsg = "[n->.]\t{}".format(message)
	print(clientMsg)
	
	# send reply
	send(address, bytesToSend)
