import eventlet
import socketio


# --- START ------------ Sending to Front-End ------------ START ---

# just some extra information when sending messages and stuff
DEBUG = True

class Hermes:
	# send raw message
	def send(self, message):
		message = str(message)
		if(DEBUG):
			print(f"[P->b]\t{message}")
		self.sio.emit("data", message)

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
	
	# send message to log
	def log(self, message):
		self.send(f"log:{message}")
	
	# send number of seconds to be registered in clock
	def clock(self, seconds):
		self.send(f"clock:{seconds}")
	
	# send gamestate
	def updateGameState(self, gameState):
		self.send(f"gameState:{gameState}")
	
	# invalid id message
	def invalidId(self, id):
		self.send(f"invalid:{id}")
	
	def __init__(self, handler):
		self.sio = socketio.Server(cors_allowed_origins="*")
		app = socketio.WSGIApp(self.sio)
		
		@self.sio.event
		def connect(sid, environ, auth):
			print("browser connected")
			if(DEBUG):
				self.sio.emit("Hello from Python")
		
		@self.sio.event
		def data(sid, x):
			if(DEBUG):
				print(f"[b->P]\t{x}")
			handler(self, x)
			#~	you were here, i think there's an issue of scope / closure
			#	where this frontEndHandler function is called in this context
			#	where hermes isn't defined
		
		@self.sio.event
		def disconnect(sid):
			print("! browser disconnected")
		
		eventlet.wsgi.server(eventlet.listen(("", 8000)), app)
	

# ---- END ------------- Sending to Front-End ------------- END ----


# --- START -------------- Socket.IO Server -------------- START ---


# ---- END --------------- Socket.IO Server --------------- END ----
