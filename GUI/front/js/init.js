function fillList(teamColor, amount, offset) {
	let container = document.getElementById(teamColor + "-team-entry-list");
	for(let i = 0; i < amount; i++) {
		let item = document.createElement("div");
		item.setAttribute("class", "list-item");
		let num = document.createElement("p");
		num.setAttribute("class", "list-number");
		num.innerHTML = zero(i + 1, 2);
		let input = document.createElement("input");
		input.setAttribute("class", "list-input");
		input.setAttribute("tabindex", offset + 2 * i);
		item.appendChild(num);
		item.appendChild(input);
		container.appendChild(item);
	}
}

window.onload = function() {
	fillList("red", 20, 1);
	fillList("green", 20, 2);
};
