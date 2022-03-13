const socket = io("http://127.0.0.1:8000");

function send(data) {
	console.log("[B->n]\t" + data);
	socket.emit("data", data);
}

function handle(field, value) {
	switch(field) {
		case "clock":
			clock(Number(value));
			break;
		case "gameState":
			gameState = Number(value);
			updateForGameState();
			break;
		case "log":
			log(value);
			break;
	}
}

socket.on("data", (data) => {
	console.log("[n->B]\t" + data);
	
	//interpret message
	let [fields, values] = twoArrays(data);
	
	//do stuff
	let stopIndex = Math.max(fields.length, values.length);
	for(let i = 0; i < stopIndex; i++) {
		let field = i < fields.length ? fields[i] : "";
		let value = i < values.length ? values[i] : "";
		handle(field, value);
	}
});
