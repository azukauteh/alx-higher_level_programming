#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}
const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected response:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
    console.log('Characters:');
    film.characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
        } else if (charResponse.statusCode !== 200) {
          console.error('Unexpected response:', charResponse.statusCode);
        } else {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  }
});
