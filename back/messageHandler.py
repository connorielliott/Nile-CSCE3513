import server
import two_arrays

playerList = []

# handle front-end messages
def frontEndHandler(msg):
	# parse message
	fields, values = two_arrays.two_arrays(msg)
	
	# interpret messages
	id = -1
	name = ""
	team = ""
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
			id = Number(value)
		elif field == "name":
			name = value
		elif field == "team":
			addPlayerToTeam((id, name), team)
			id = -1
			name = ""
			team = ""
		elif field == "gameState" and value == "1":
			startGame()

# handle networking messages
def networkingHandler(msg):
	# to be implemented
	print("handling network messages dutifully.")
