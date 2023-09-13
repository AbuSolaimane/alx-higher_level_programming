#!/usr/bin/node

const dict = require('./101-data').dict;
const myDict = {};

for (const ele in dict) {
  const occurrence = dict[ele];
  if (!myDict[occurrence]) {
    myDict[occurrence] = [];
  }
  myDict[occurrence].push(ele.toString());
}
console.log(myDict);
