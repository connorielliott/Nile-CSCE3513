var gameState = 0;
var currentScreenId = "player-entry-screen";
var f1Good = true,
	f5Good = true;

//player entry stuff
function F1() {
	//when gamestate is 0, switch to player entry screen
	//if already on this screen, clear player entry data
	if(!(f1Good && gameState == 0)) return;
	if(currentScreenId === "player-entry-screen") {
		clearInputs();
	}
	clearPlayers();
	score("red", 0);
	score("green", 0);
	switchToScreen("player-entry-screen");
}

function clearInputs() {
	let inputs = document.getElementsByClassName("list-input");
	for(let i = 0; i < inputs.length; i++) {
		inputs[i].value = "";
	}
}

function highlight(id) {
	let idInputs = document.getElementsByClassName("list-input-id");
	for(let i = 0; i < idInputs.length; i++) {
		if(Number(idInputs[i].value.trim()) == id) {
			//~	more animation here or smth
			idInputs[i].focus();
			alert("Please check this id and name pair.");
		}
	}
}


//play action stuff
function F5() {
	//when gamestate is 0, check if player entries are valid and switch gamestate to 1 if good
	//also switch to play action screen
	if(!(f5Good && gameState == 0 && currentScreenId == "player-entry-screen" && goodEntries())) {
		return;
	}
	
	//send user infos
	let idInputs = document.getElementsByClassName("list-input-id"),
		nameInputs = document.getElementsByClassName("list-input-name");
	for(let i = 0; i < idInputs.length; i++) {
		let id = idInputs[i].value.trim(),
			name = nameInputs[i].value.trim();
		if(!goodEntry(id, name)) continue;
		let fields = [],
			values = [];
		if(id != "") {
			fields.push("id");
			values.push(id);
		}
		if(name.length > 0) {
			fields.push("name");
			values.push(name);
		}
		fields.push("team");
		values.push(idInputs[i].getAttribute("class").indexOf("red") > -1 ? "red" : "green");
		send(fvFormat(fields, values));
	}
	
	//send gameState update
	send("gameState:1");
}

//displaying messages and info stuff
function state(message) {
	document.getElementById("state").innerHTML = message;
	log(message);
}
function substate(message) {
	document.getElementById("substate").innerHTML = message;
	log(message);
}

function clock(seconds) {
	let [mins, secs] = timeFromSeconds(seconds);
	document.getElementById("clock").innerHTML = zero(mins, 2) + ":" + zero(secs, 2);
	//for auto-switch to play action screen if disconnected
	switchToScreen("play-action-screen");
}

function score(team, skore) {
	document.getElementById(team + "-team-title-score").innerHTML = team.toUpperCase() + " Team - " + skore;
}

function clearLog() {
	document.getElementById("log").innerHTML = "";
}
function log(message) {
	let li = document.createElement("li");
	li.setAttribute("class", "log-message");
	li.innerHTML = message;
	document.getElementById("log").appendChild(li);
	li.scrollIntoView();
}
function clearActionLog() {
	document.getElementById("action-list").innerHTML = "";
}
function actionLog(message) {
	let li = document.createElement("li");
	li.setAttribute("class", "action-message");
	li.innerHTML = message;
	document.getElementById("action-list").appendChild(li);
	li.scrollIntoView();
}

function clearPlayers() {
	document.getElementById("red-team-list").innerHTML = "";
	document.getElementById("green-team-list").innerHTML = "";
}
function addPlayer(name, team) {
	let li = document.createElement("li");
	li.setAttribute("class", "player " + team + "-player");
	li.innerHTML = name;
	document.getElementById(team + "-team-list").appendChild(li);
}

function clearActionScreen() {
	clearPlayers();
	clearLog();
	clearActionLog();
}


//game state management
function updateForGameState() {
	switch(gameState) {
		case 0:
			state("Game Inactive.");
			enableButton("f1");
			enableButton("f5");
			break;
		case 1:
			state("Game Starting Soon!");
			disableButton("f1");
			disableButton("f5");
			switchToScreen("play-action-screen");
			break;
		case 2:
			state("Game Active!");
			break;
	}
}

//screen management
function switchToScreen(id) {
	switch(id) {
		case "player-entry-screen":
			modButton("f1", "Clear Team Data");
			modButton("f5", "Start Game");
			break;
		case "play-action-screen":
			modButton("f1", "Return to Player Entry Screen");
			modButton("f5", "Do Nothing");
			break;
	}
	if(id == currentScreenId) return;
	let screens = document.getElementsByClassName("screen");
	for(let i = 0; i < screens.length; i++) {
		if(screens[i].id !== id) {
			screens[i].style.display = "none";
			continue;
		}
		screens[i].style.display = "grid";
		currentScreenId = screens[i].id;
	}
}

//button management
function enableButton(f) {
	document.getElementById(f + "-button").removeAttribute("disabled");
	switch(f) {
		case "f1":
			f1Good = true;
			break;
		case "f5":
			f5Good = true;
			break;
	}
}
function disableButton(f) {
	document.getElementById(f + "-button").setAttribute("disabled", "");
	switch(f) {
		case "f1":
			f1Good = false;
			break;
		case "f5":
			f5Good = false;
			break;
	}
}
function modButton(f, actionMessage) {
	document.getElementById(f + "-button").innerHTML = f.toUpperCase() + " to " + actionMessage;
}


//keypress
window.onkeydown = (ev) => {
	if(ev.keyCode >= 112 && ev.keyCode <= 123) {
		ev.preventDefault();
	}
	switch(ev.keyCode) {
		case 112:
			F1();
			break;
		case 116:
			F5();
			break;
	}
};
