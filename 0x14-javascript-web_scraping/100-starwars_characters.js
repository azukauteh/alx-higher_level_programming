#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
if (!filmId) {
  console.log('Usage: ./100-starwars_characters.js <film_id>');
  process.exit(1);
}
const url = 'https://swapi.dev/api/films/' + filmId;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    try {
      // Attempt to parse the response body as JSON
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
