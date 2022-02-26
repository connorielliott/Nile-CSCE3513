var gameActive = false;
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
	if(gameActive) return;
	clearInputs();
	switchToScreen("player-entry-screen");
}

function F3() {
	//after all players entered, f3 key will move to play action screen for rest of game
	if(currentScreenId !== "play-action-screen") {
		switchToScreen("play-action-screen");
		document.getElementById("f3-button").innerHTML = "F3 to Start Game";
	}
	else {
		//
	}
	//~	send("start game");
	gameActive = true;
}

window.onkeydown = (ev) => {
	if(ev.keyCode >= 112 && ev.keyCode <= 123) {
		ev.preventDefault();
	}
	switch(ev.keyCode) {
		case 112:
			F1();
			break;
		case 114:
			F3();
			break;
	}
};
