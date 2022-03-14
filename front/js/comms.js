const socket = io("http://127.0.0.1:8000");

function send(data) {
	console.log("[B->n]\t" + data);
	socket.emit("data", data);
}

function twoArrays(str) {
    let arrayswitch = true
    let array1 = new Array();
    let array2 = new Array();
    let array3 = new Array();
    for (let i = 0; i < str.length; i++) {
        if ((str.charAt(i) === ':') || (str.charAt(i) === ','))
        {
            arrayswitch = !arrayswitch;
        }
        if (arrayswitch === true)
        {
            if ((str.charAt(i) === ':') || (str.charAt(i) === ',') || (str.charAt(i) === ' '))
            {
            }
            else
            {
                array1 += str.charAt(i)
            }
        }
        else
        {
            if ((str.charAt(i) === ':') || (str.charAt(i) === ',') || (str.charAt(i) === ' '))
            {
            }
            else
            {
                array2 += str.charAt(i)
            }
        }
    }
    array3 = array1 + '/' + array2;
    return array3;
}
//    code to test above function
//    let str = "a:1, b:2, c:3";
//    let array = twoArrays(str);
//    print(array.toString());

socket.on("data", (data) => {
	console.log("[n->B]\t" + data);
	
	//interpret message
	let [fields, values] = twoArrays(data);
	
	//do stuff
	let stopIndex = Math.max(fields.length, values.length);
	let name = "",
		team = "";
	for(let i = 0; i < stopIndex; i++) {
		let field = i < fields.length ? fields[i] : "";
		let value = i < values.length ? values[i] : "";
		switch(field) {
			case "clock":
				clock(Number(value));
				break;
			case "gameState":
				gameState = Number(value);
				updateForGameState();
				break;
			case "invalid":
				highlight(Number(value));
				break;
			case "log":
				log(value);
				break;
			case "name":
				name = value;
				break;
			case "team":
				team = value;
				addPlayer(name, team);
				name = "";
				team = "";
				break;
		}
	}
});
