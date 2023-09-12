#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sortedArgs = process.argv
    .slice(2, process.argv.length)
    .map(parseInt)
    .sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
