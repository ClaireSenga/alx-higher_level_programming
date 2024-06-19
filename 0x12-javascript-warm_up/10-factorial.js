#!/usr/bin/node
// A script that computes a factorial recursively

// Recursive function
function factorial(n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Get the first arg & parse it as an int
const arg1 = process.argv[2];
const int1 = parseInt(arg1);

// Check if the arg is NaN & handle it
if (isNaN(int1)) {
  console.log(1);
} else {
  console.log(factorial(int1));
}
