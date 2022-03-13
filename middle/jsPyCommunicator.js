//https://stackoverflow.com/a/61693174
//https://stackoverflow.com/a/38749535

const dgram = require("dgram");
const http = require("http");
const socketio = require("socket.io");

//debug
const DEBUG = false;

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
	if(DEBUG) console.log(`[N->b]\t${data}`);
	io.emit("data", data);
}

//browser listen / send
io.on("connection", (socket) => {
	console.log(`browser connected`);
	//sendToBrowser(`Hello from NodeJS`);
	
	socket.on("data", (data) => {
		if(DEBUG) console.log(`[b->N]\t${data}`);
		
		//relay to python
		sendToPython(data);
	});
	
	socket.on("disconnect", () => {
		console.log(`! browser disconnected`);
	});
});


//send to python
function sendToPython(data) {
	if(DEBUG) console.log(`[N->p]\t${data}`);
	client.send(Buffer.from(data.toString()), 20001, "127.0.0.1", (err) => {
		if(err){}	//don't care
	});
}

//python send
sendToPython(`Hello from NodeJS`);

//python listen
client.on("message", (msg, info) => {
	if(DEBUG) console.log(`[p->N]\t${msg.toString()}`);
	sendToBrowser(msg.toString());
});
