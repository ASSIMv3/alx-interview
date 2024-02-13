#!/usr/bin/node
const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];

if (!filmId) {
  console.log('Please provide a film ID as argument.');
  process.exit(1);
}

request(URL + filmId + '/', (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  } else if (res.statusCode !== 200) {
    console.error('Error:', res.statusCode);
    return;
  }

  body = JSON.parse(body);

  const charactersLength = body.characters.length;
  let printed = 0;

  const printCharacter = (characterUrl) => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      } else if (res.statusCode !== 200) {
        console.error('Error:', res.statusCode);
        return;
      }

      body = JSON.parse(body);
      console.log(body.name);
      printed++;

      if (printed === charactersLength) {
        process.exit(0); // Exit when all characters are printed
      }
    });
  };

  // Print characters
  body.characters.forEach(characterUrl => printCharacter(characterUrl));
});
