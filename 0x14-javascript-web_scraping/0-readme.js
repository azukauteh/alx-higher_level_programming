#!/usr/bin/node
// This script reads the content of a file specified as a command line argument (process.argv[2]).
// It uses the 'fs' (File System) module to read the file and prints the content to the console.
// If there is an error while reading the file, it will be displayed; otherwise, the file's content is printed.
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
