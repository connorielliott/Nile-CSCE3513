# these are ours
import two_arrays
import main


# --- START -------------- Message Handlers -------------- START ---

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
			main.addPlayerToTeam(id, name, value)
			id = -1
			name = ""
		elif field == "gameState" and value == "1":
			main.startGame()


# handle networking messages
def traffic(msg):
	print(f"traffic: {msg}")

	if(main.gameState != 2):
		return

	# get killer and killed int IDs
	[killerId, killedId] = msg.split(":")
	killerId = int(killerId)
	killedId = int(killedId)
	
	# get killer and killed teams and names
	(killerTeam, killerName) = main.getPlayer(killerId)
	(killedTeam, killedName) = main.getPlayer(killedId)

	# increment score appropriately
	if(killerTeam == "red"):
		main.incrementScore("red")
	elif(killerTeam == "green"):
		main.incrementScore("green")
	
	# display scores
	main.display.score("red", main.redScore)
	main.display.score("green", main.greenScore)

	# send kill message
	main.display.kill(killerTeam, killerName, killedTeam, killedName)

# ---- END --------------- Message Handlers --------------- END ----
