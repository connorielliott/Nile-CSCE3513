import socket


# --- START --------------- Configuration ---------------- START ---

localIP     = "127.0.0.1"
recv_port = 7501
broadcast_port = 7500
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, recv_port))

# ---- END --------------- Configuration ---------------- END ----


# --- START ------- Functions for Usage Elsewhere -------- START ---

def broadcast(message):
	UDPServerSocket.sendto(str.encode(message), broadcast_port)

# ---- END -------- Functions for Usage Elsewhere --------- END ----


# Listen for incoming datagrams
def listen():
	print("entering listening loop...")
	while(True):
		# wait for message
		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
		message = bytesAddressPair[0]
		address = bytesAddressPair[1]
		
		message = str(message)[2:-1]
		print(f"received:\t{message}")
		
		trafficHandler(message)


# start function
def start():
	try:
		print("starting listening thread...")
		listen()
	except Exception as e:
		print("! failed listening thread:")
		print(e)
