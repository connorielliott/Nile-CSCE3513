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
	//when game ends, stay on play action screen until f1 pressed. it will clear out player data and return to player input screen
	if(gameState != 0) return;
	if(currentScreenId === "player-entry-screen") {
		clearInputs();
	}
	switchToScreen("player-entry-screen");
}

function F5() {
	//after all players entered, f5 key will move to play action screen for rest of game
	if(!checkEnoughPlayers()) {
		return;
	}
	
	//send user infos
	//~	you were here
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
		}
		else {
			fields.push("dba");
			values.push("modify");
			fields.push("name");
			fields.push(nameInputs[i].value.trim());
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
