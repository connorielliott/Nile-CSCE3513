function zero(x, d) {
	let y;
	for(y = x.toString(); y.length < d; y = '0' + y);
	return y;
}

function fvFormat(fields, values) {
	const stopIndex = Math.max(fields.length, values.length);
	let string = "";
	for(let i = 0; i < stopIndex; i++) {
		field = i < fields.length ? fields[i] : "";
		value = i < values.length ? values[i] : "";
		string += field + ":" + value;
		if(i < stopIndex - 1) string += ",";
	}
	return string;
}

function checkEnoughPlayers() {
	//test if player entry data is good enough to start game
	let redIdInputs = document.getElementsByClassName("list-input-team-red"),
		greenIdInputs = document.getElementsByClassName("list-input-team-green");
	let redGood = false,
		greenGood = false;
	for(let i = 0; i < redIdInputs.length; i++) {
		if(redIdInputs[i].value.length == 0 || typeof Number(redIdInputs[i].value) == "NaN") {
			redGood = true;
			break;
		}
	}
	for(let i = 0; i < greenIdInputs.length; i++) {
		if(greenIdInputs[i].value.length == 0 || typeof Number(greenIdInputs[i].value) == "NaN") {
			greenGood = true;
			break;
		}
	}
	return redGood && greenGood;
}

function twoArrays(str) {
	let result = [];
	let pairs = str.split(",").map((e) => { return e.trim(); });
	let fields = pairs.map((e) => { return e.substring(0, e.indexOf(":")); }),
		values = pairs.map((e) => { return e.substring(e.indexOf(":") + 1); });
	return [fields, values];
}
