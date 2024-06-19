#!/usr/bin/node
// A script that prints the first argument passed (process.argv[2])
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
