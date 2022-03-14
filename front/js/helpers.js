function goodEntry(idValue, nameValue) {
	//just makes sure that only one box can be empty
	//and that id, if provided, is a number
	if(idValue.length == 0) {
		return nameValue.length != 0;
	}
	return typeof Number(idValue) != "NaN";
}

function goodEntries() {
	//see if each team has at least one good entry
	//
	//for(let i = 0; i < .length; i++) {
	//	if(goodEntry(i))
	//}
	//return redGood && greenGood;
	return true;
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

function timeFromSeconds(seconds) {
	//only up to minutes, not hours
	return [Math.floor(seconds / 60), seconds % 60];
}

function twoArrays(str) {
	let result = [];
	let pairs = str.split(",").map((e) => { return e.trim(); });
	let fields = pairs.map((e) => { return e.substring(0, e.indexOf(":")); }),
		values = pairs.map((e) => { return e.substring(e.indexOf(":") + 1); });
	return [fields, values];
}

function zero(x, d) {
	let y;
	for(y = x.toString(); y.length < d; y = '0' + y);
	return y;
}
