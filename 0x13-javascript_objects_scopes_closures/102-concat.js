#!/usr/bin/node

const file1 = process.argv[2];
const file2 = process.argv[3];
const destinationFile = process.argv[4];

const fs = require('fs');

const file1Data = fs.readFileSync(file1, 'utf8');
const file2Data = fs.readFileSync(file2, 'utf8');
const concatenatedData = file1Data + file2Data;
fs.writeFileSync(destinationFile, concatenatedData);
