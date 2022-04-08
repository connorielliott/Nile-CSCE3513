import eventlet
import socketio


# --- START ------------ Sending to Front-End ------------ START ---

# just some extra information when sending messages and stuff
DEBUG = False

class Hermes:
	def __init__(self, sio):
		self.sio = sio
	
	# send raw message
	def send(message):
		message = str(message)
		if(DEBUG):
			print(f"[P->b]\t{message}")
		self.sio.emit("data", message)

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
		send(f"log:{message}")

	# send number of seconds to be registered in clock
	def clock(seconds):
		send(f"clock:{seconds}")

	# send gamestate
	def updateGameState(gameState):
		send(f"gameState:{gameState}")

	# invalid id message
	def invalidId(id):
		send(f"invalid:{id}")

# ---- END ------------- Sending to Front-End ------------- END ----


# --- START -------------- Socket.IO Server -------------- START ---

def initHermes(handler):
	sio = socketio.Server(cors_allowed_origins="*")
	app = socketio.WSGIApp(sio)

	@sio.event
	def connect(sid, environ, auth):
		print("browser connected")
		if(DEBUG):
			send("Hello from Python")

	@sio.event
	def data(sid, x):
		if(DEBUG):
			print(f"[b->P]\t{x}")
		handler(x)

	@sio.event
	def disconnect(sid):
		print("! browser disconnected")

	eventlet.wsgi.server(eventlet.listen(("", 8000)), app)
	
	hermes = Hermes(sio)
	return hermes

# ---- END --------------- Socket.IO Server --------------- END ----
