#!/usr/bin/node
const fs = require('fs');

// Check if both file path and string are provided as arguments
if (process.argv.length < 4) {
  console.log('Usage: ./write-file.js <file_path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file in utf-8 encoding
fs.writeFile(filePath, content, error => {
  if (error) {
    console.log(error); // Print the error object if an error occurs
  }
});

