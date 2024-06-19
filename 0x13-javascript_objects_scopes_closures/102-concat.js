#!/usr/bin/node

const fs = require('fs');

function concatFiles(sourceFile1, sourceFile2, destinationFile) {

  fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
    if (err1) {
      console.error(`Error reading ${sourceFile1}: ${err1.message}`);
      return;
    }

    fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
      if (err2) {
        console.error(`Error reading ${sourceFile2}: ${err2.message}`);
        return;
      }

      // Concatenate the contents of the two files
      const concatenatedData = data1 + data2;

      fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
        if (err) {
          console.error(`Error writing to ${destinationFile}: ${err.message}`);
        } else {
          console.log(`Successfully concatenated ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
        }
      });
    });
  });
}

if (process.argv.length !== 5) {
  console.error('Usage: node concatFiles.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

concatFiles(sourceFile1, sourceFile2, destinationFile);
