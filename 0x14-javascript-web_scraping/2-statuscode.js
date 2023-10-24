#!/usr/bin/node
const request = require('request');

// Check if a URL is provided as an argument
if (process.argv.length < 3) {
  console.log('Usage: ./http-status.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Send an HTTP GET request to the specified URL
request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`); // Log the HTTP status code of the response
});
