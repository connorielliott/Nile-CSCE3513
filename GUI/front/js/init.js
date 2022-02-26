function fillList(teamColor, amount, offset) {
	let container = document.getElementById(teamColor + "-team-entry-list");
	for(let i = 0; i < amount; i++) {
		let item = document.createElement("div");
		item.setAttribute("class", "list-item");
		let num = document.createElement("p");
		num.setAttribute("class", "list-number");
		num.innerHTML = zero(i + 1, 2);
		let input_id = document.createElement("input");
		input_id.setAttribute("class", "list-input list-input-id");
		input_id.setAttribute("tabindex", offset + 4 * i);
		input_id.setAttribute("placeholder", "User ID Number");
		let input_name = document.createElement("input");
		input_name.setAttribute("class", "list-input list-input-name");
		input_name.setAttribute("tabindex", offset + 4 * i + 1);
		input_name.setAttribute("placeholder", "Code Name");
		item.appendChild(num);
		item.appendChild(input_id);
		item.appendChild(input_name);
		container.appendChild(item);
	}
}

window.onload = function() {
	fillList("red", 15, 1);
	fillList("green", 15, 3);
};
