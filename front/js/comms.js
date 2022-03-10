const socket = io("http://127.0.0.1:8000");

function send(data) {
	console.log("[B->n]\t" + data);
	socket.emit("data", data);
}

socket.on("data", (data) => {
	console.log("[n->B]\t" + data);
	
	//do stuff with data
	//
});
