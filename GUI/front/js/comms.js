const socket = io("http://127.0.0.1:8000");

function send(data) {
	socket.emit("data", data);
	console.log("[.->n]\t" + data);
}

socket.on("data", (data) => {
	console.log("[n->.]\t" + data);
	
	//do stuff with data
	//
});
