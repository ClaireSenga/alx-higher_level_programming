#!/usr/bin/node
// a script that prints 2 args passed

if (process.argv[2] && process.argv[3]) {
    console.log(`${process.argv[2]} is ${process.argv[3]}`);
}
else {
    console.log("Missing arguments");
}
