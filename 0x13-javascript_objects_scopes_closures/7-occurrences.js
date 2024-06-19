#!/usr/bin/node
// Define the function nbOccurences
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  
  // Loop through each element in the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element matches the searchElement
    if (list[i] === searchElement) {
      count++;
    }
  }
  
  return count;
};
