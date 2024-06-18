#!/usr/bin/node
//prints a square
const square = process.argv[2];
const arg = parseInt(square);
if (isNaN(arg)) {
	console.log("Missing Size");
}
else {
	for (let i = 0; i < arg;
		i++) {
		let row = "";
	for (let j = 0; j < arg;
		j++) {
		row += "X";
	}
	console.log(row);
	}
}
