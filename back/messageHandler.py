import server
import two_arrays


# handle front-end messages
def frontEnd(msg):
	# parse message
	parsed = two_arrays.two_arrays(msg)
	fields = parsed[0]
	values = parsed[1]
	
	# interpret messages
	id = -1
	name = ""
	stopIndex = max(len(fields), len(values))
	for i in range(0, stopIndex):
		if i < len(fields):
			field = fields[i]
		else:
			field = ""
		if i < len(values):
			value = values[i]
		else:
			value = ""

		# the only possible messages are for player entry and to start the game
		# both of these are only possible when gamestate is 0
		if field == "id":
			id = int(value)
		elif field == "name":
			name = value
		elif field == "team":
			addPlayerToTeam((id, name), value)
			id = -1
			name = ""
		elif field == "gameState" and value == "1":
			startGame()


# handle networking messages
def networking(msg):
	# to be implemented
	print("handling network messages dutifully.")
	print(f"message sent from client: {msg}")


# must be before all server.send(<str>) usages since this gets the address of the bridge
def initDisplay():
	return server.start(frontEnd, networking)

# keep down here to fix circular import issue
from main import startGame, addPlayerToTeam
