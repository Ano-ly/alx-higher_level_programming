#!/usr/bin/node

const myArg = process.argv;
let i;
const x = Number(myArg[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
