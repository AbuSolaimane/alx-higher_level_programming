#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const myUrl = `https://swapi.dev/api/films/${movieId}/`;
let characters = [];

req(myUrl, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  characters = data.characters;
  getCharacters(0);
});
const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }
  req(characters[index], (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
