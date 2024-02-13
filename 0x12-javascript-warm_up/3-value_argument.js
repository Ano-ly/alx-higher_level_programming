#!/usr/bin/node

let len = 0;
const myArg = process.argv;

myArg.forEach((val, index) => {
  len++;
});

if (len === 2) {
  console.log('No argument');
} else {
  console.log(myArg[2]);
}
