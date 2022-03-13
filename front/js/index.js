var gameState = 0;
var currentScreenId = "player-entry-screen";

function switchToScreen(id) {
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

function clearInputs() {
	let inputs = document.getElementsByClassName("list-input");
	for(let i = 0; i < inputs.length; i++) {
		inputs[i].value = "";
	}
}

function F1() {
	//when gamestate is 0, switch to player entry screen
	//if already on this screen, clear player entry data
	if(gameState != 0) return;
	if(currentScreenId === "player-entry-screen") {
		clearInputs();
	}
	switchToScreen("player-entry-screen");
}

function F5() {
	//when gamestate is 0, check if player entries are valid and switch gamestate to 1 if good
	//also switch to play action screen
	if(gameState != 0 || !checkEnoughPlayers()) {
		return;
	}
	
	//send user infos
	//~	make better checks for valid player entry data
	let idInputs = document.getElementsByClassName("list-input-id"),
		nameInputs = document.getElementsByClassName("list-input-name");
	for(let i = 0; i < idInputs.length; i++) {
		if(idInputs[i].value.trim().length == 0 || typeof Number(idInputs[i].value) == "NaN") continue;
		let fields = [],
			values = [];
		fields.push("id");
		values.push(idInputs[i].value.trim());
		if(nameInputs[i].value.trim().length == 0) {
			fields.push("dba");
			values.push("query");
			fields.push("query");
			values.push("name");
		}
		else {
			fields.push("dba");
			values.push("modify");
			fields.push("name");
			values.push(nameInputs[i].value.trim());
		}
		send(fvFormat(fields, values));
	}
	
	//send gameState update
	send("gameState:1");
	
	//switch to play action screen
	if(currentScreenId !== "play-action-screen") {
		switchToScreen("play-action-screen");
	}
}

function log(message) {
	let li = document.createElement("li");
	li.setAttribute("class", "log-message");
	li.innerHTML = message;
	document.getElementById("log").appendChild(li);
}

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
