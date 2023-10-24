#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const myUrl = `https://swapi.dev/api/films/${movieId}/`;

req.get(myUrl, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    req(character, (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
