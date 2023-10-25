#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected response:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characterUrls = film.characters;
    // Function to retrieve and print character names sequentially
    const printCharacters = (index) => {
      if (index < characterUrls.length) {
        request(characterUrls[index], (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('Unexpected response:', charResponse.statusCode);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
            // Continue with the next character
            printCharacters(index + 1);
          }
        });
      }
    };

    console.log(film.title);
    console.log('Characters:');
    // Start with the first character
    printCharacters(0);
  }
});
