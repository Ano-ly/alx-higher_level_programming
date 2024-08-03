#!/usr/bin/node

let num;
if (process.argv.length <= 2) {
  num = NaN;
} else {
  num = process.argv[2];
}

function fact (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }
  return num * fact(num - 1);
}

console.log(fact(num));
