#!/usr/bin/node
// Script that prints arg converted to int
const arg = process.argv[2];
const intValue = parseInt(arg);

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log("My number: " + intValue);
}
