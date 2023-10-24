#!/usr/bin/node
const request = require('request');

// Construct the URL for the Star Wars API.
const url = 'http://swapi.co/api/films/' + process.argv[2];

// Send an HTTP GET request to the specified UR.
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
