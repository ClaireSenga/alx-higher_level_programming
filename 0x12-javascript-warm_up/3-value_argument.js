#!/usr/bin/node
//a script that prints 1st arg passed

if (process.argv[2]) {
	console.log(process.argv[2]);
	}
else {
	console.log('No argument');
}
