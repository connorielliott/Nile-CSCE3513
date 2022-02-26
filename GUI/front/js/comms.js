const socket = io("http://127.0.0.1:8000");

function send(msg) {
	socket.emit("data", msg);
	console.log("[to:nodejs] " + msg);
}

socket.on("data", (data) => {
	switch(data.)
	console.log("[fr:nodejs] " + data);
});
