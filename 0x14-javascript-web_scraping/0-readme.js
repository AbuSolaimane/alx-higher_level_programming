#!/usr/bin/node

const fileSystem = require('fs');
const filename = process.argv[2];

fileSystem.readFile(filename, (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
