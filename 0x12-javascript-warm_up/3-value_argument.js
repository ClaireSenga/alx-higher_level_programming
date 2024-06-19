#!/usr/bin/node
// A script that prints 1st arg passed (process.argv[2])
if (process.argv[2]) {
	console.log(process.argv[2]);
} else {
	console.log('No argument');
}
