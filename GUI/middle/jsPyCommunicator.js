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


//send to browser
function sendToBrowser(data) {
	io.emit("data", data);
	console.log(`[.->b]\t${data}`);
}

//browser listen / send
io.on("connection", (socket) => {
	sendToBrowser(`Hello from NodeJS!`);
	
	socket.on("data", (data) => {
		console.log(`[b->.]\t${data}`);
		
		//relay to python
		sendToPython(data);
	});
	
	socket.on("disconnect", () => {
		console.log(`! browser disconnected`);
	});
});


//send to python
function sendToPython(data) {
	client.send(Buffer.from(data), 20001, "127.0.0.1", (err) => {
		if(err) {
			console.error(`! [.->p]\t${err}`);
		}
		else {
			console.log(`[.->p]\t${data}`);
		}
	});
}

//python send
sendToPython(`Hello from NodeJS`);

//python listen
client.on("message", (msg, info) => {
	sendToBrowser(msg.toString());
	console.log(`[p->.]\t${msg.toString()}`);
});
