const socket = io("http://127.0.0.1:8000");

function send(data) {
	console.log("[B->n]\t" + data);
	socket.emit("data", data);
}

socket.on("data", (data) => {
	console.log("[n->B]\t" + data);
	
	//interpret message
	//
	
	//do stuff
	//for(let i = 0; i < Math.max(fieldArray.length, valueArray.length); i++) {
		//
	//}
});
