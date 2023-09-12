#!/usr/bin/node
const MySquare = require('./5-square');

class Square extends MySquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      for (let j = 0; j < this.width; j++) {
        myVar += (c === undefined ? 'X' : c);
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
