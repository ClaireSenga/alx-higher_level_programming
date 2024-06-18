#!/usr/bin/node
//prints x times a string
const x = process.argv[2];
const arg = parseInt(x);
if (isNaN(arg)) {
	console.log("Missing number of occurrences");	
} else {
	for (let i = 0; i < arg; i++) {
	console.log("C is fun");
}
}
