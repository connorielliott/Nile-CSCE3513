import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ, auth):
	print("connect", sid)


@sio.on("data")
def receiveFromFrontEnd(sid, data):
	sio.emit("data", "hey")
	print("data", data)

eventlet.wsgi.server(eventlet.listen(("", 8000)), app)
