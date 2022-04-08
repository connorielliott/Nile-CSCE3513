# these are ours
import two_arrays
from main import startGame, addPlayerToTeam

# --- START ---------- Receiving from Front-End ---------- START ---

playerList = []

# handle front-end messages
def frontEndHandler(msg):
	# parse message
	fields = two_arrays.two_arrays(msg)[0]
	values = two_arrays.two_arrays(msg)[1]
	
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

# ---- END ----------- Receiving from Front-End ----------- END ----


# handle traffic data
def trafficHandler(msg):
	# to be implemented
	print("handling traffic dutifully.")
	print(f"message sent from client: {msg}")
