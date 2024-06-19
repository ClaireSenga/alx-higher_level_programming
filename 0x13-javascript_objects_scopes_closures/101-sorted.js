#!/usr/bin/node

const { dict } = require('./101-data'); // Adjust the path as necessary

// Function to compute occurrences dictionary
function computeOccurrencesDict(dict) {
  const occurrencesDict = {};

  for (const userId in dict) {
    const occurrences = dict[userId];

    if (!occurrencesDict[occurrences]) {
      occurrencesDict[occurrences] = [];
    }

    occurrencesDict[occurrences].push(userId);
  }

  return occurrencesDict;
}

const occurrencesDict = computeOccurrencesDict(dict);

console.log(occurrencesDict);
