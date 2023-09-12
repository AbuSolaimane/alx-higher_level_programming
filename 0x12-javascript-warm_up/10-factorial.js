#!/usr/bin/node
function factorial (n) {
  return isNaN(n) || n === 0 ? 1 : n * factorial(n - 1);
}i

console.log(factorial(parseInt(process.argv[2])));
