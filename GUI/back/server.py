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

# Listen for incoming datagrams
while(True):
	
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	clientMsg = "[fr:nodejs] {}".format(message)
	
	print(clientMsg)
	
	# Sending a reply to client
	UDPServerSocket.sendto(bytesToSend, address)
	print("[to:nodejs]", bytesToSend)
