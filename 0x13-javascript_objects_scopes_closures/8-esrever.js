#!/usr/bin/node
// Define the function esrever
exports.esrever = function (list) {

  let start = 0;
  let end = list.length - 1;
  
  while (start < end) {
    // Swap elements at start and end pointers
    let temp = list[start];
    list[start] = list[end];
    list[end] = temp;
    
    // Move pointers towards center
    start++;
    end--;
  }
  
  return list;
};
