#!/usr/bin/node
const req = require('request');
const myUrl = process.argv[2];

req.get(myUrl, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
