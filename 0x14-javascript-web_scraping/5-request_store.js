#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const myUrl = process.argv[2];
const file = process.argv[3];

req(myUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
