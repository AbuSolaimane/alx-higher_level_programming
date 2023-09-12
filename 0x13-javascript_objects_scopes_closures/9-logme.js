#!/usr/bin/node

let myCount = 0;

exports.logMe = function count (item) {
  console.log(myCount + ': ' + item);
  myCount += 1;
};
