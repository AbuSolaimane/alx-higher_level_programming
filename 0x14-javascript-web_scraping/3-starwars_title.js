#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const myUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(myUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
