#!/usr/bin/node

const req = require('request');
const myUrl = process.argv[2];
const characterId = '18';
let count = 0;

req.get(myUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
