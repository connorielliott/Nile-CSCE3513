const socket = io("http://127.0.0.1:8000");

const DEBUG = true;

function send(data) {
	if(DEBUG) console.log("[B->n]\t" + data);
	socket.emit("data", data);
}

socket.on("data", (data) => {
	if(DEBUG) console.log("[n->B]\t" + data);
	
	//interpret message
	let [fields, values] = twoArrays(data);
	
	//do stuff
	let stopIndex = Math.max(fields.length, values.length);
	let name = "",
		skore = -1,
		team = "";
	let killed = {},
		killer = {};
	for(let i = 0; i < stopIndex; i++) {
		let field = i < fields.length ? fields[i] : "";
		let value = i < values.length ? values[i] : "";
		switch(field) {
			case "clock":
				clock(Number(value));
				break;
			case "gameState":
				gameState = Number(value);
				updateForGameState();
				break;
			case "invalid":
				highlight(Number(value));
				clearPlayers();
				break;
			case "killed":
				killed.name = value;
				break;
			case "killedTeam":
				killed.team = value;
				break;
			case "killer":
				killer.name = value;
				break;
			case "killerTeam":
				killer.team = value;
				let message = `<span class="${killer.team}-text">${killer.name}</span> tagged <span class="${killed.team}-text">${killed.name}</span>!`;
				actionLog(message);
				killed = {};
				killer = {};
				break;
			case "log":
				log(value);
				break;
			case "name":
				name = value;
				break;
			case "score":
				skore = Number(value);
				break;
			case "state":
				substate(value);
				break;
			case "team":
				team = value;
				if(name != "") {
					addPlayer(name, team);
					name = "";
				}
				else if(skore != -1) {
					score(team, skore);
					skore = -1;
				}
				team = "";
				break;
		}
	}
});
