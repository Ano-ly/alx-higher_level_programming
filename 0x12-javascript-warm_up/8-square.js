#!/usr/bin/node

const myArg = process.argv;
let i;
let j;
let str;

const size = Number(myArg[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    str = '';
    for (j = 0; j < size; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
