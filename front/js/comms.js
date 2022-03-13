const socket = io("http://127.0.0.1:8000");

function send(data) {
	console.log("[B->n]\t" + data);
	socket.emit("data", data);
}

socket.on("data", (data) => {
	console.log("[n->B]\t" + data);
	
	//interpret message
	let parsedData = twoArrays(data);
	let fields = parsedData[0],
		values = parsedData[1];
	
	//do stuff
	let stopIndex = Math.max(fieldArray.length, valueArray.length);
	for(let i = 0; i < stopIndex; i++) {
		//
	}
});
