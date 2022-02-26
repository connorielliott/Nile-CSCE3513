//https://stackoverflow.com/a/61693174
//https://stackoverflow.com/a/38749535

const dgram = require("dgram");
const http = require("http");
const socketio = require("socket.io");

//connect to python server
const client = dgram.createSocket("udp4");

//setup socket server for browser
const server = http.createServer((req, res) => {});
server.listen(8000);
const io = socketio(server, {
	cors: {
		origin: "*"
	}
});

//browser listen / send
io.on("connection", (socket) => {
	socket.emit("data", "Hello from NodeJS!");
	
	socket.on("data", (data) => {
		console.log(`[fr:browsr] ${data}`);
	});
	
	socket.on("disconnect", () => {
	});
});


//python send
const data = Buffer.from(`Hello from NodeJS`);
client.send(data, 20001, "127.0.0.1", (err) => {
	if(err) {
		console.error(`[to:python] fail: ${err}`);
	}
	else {
		console.log(`[to:python] sent: ${data}`);
	}
});


//python listen
client.on("message", (msg, info) => {
	console.log(`[fr:python] recv: ${msg.toString()}`);
	console.log(`[fr:python] info: ${info.toString()}`);
});
