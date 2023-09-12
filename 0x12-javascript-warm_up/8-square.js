#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  const columnSize = parseInt(size);
  for (let i = 0; i < columnSize; i++) {
    let row = '';
    for (let j = 0; j < columnSize; j++) row += 'X';
    console.log(row);
  }
}
