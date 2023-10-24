#!/usr/bin/node

const fileSystem = require('fs');
const filename = process.argv[2];

fileSystem.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
