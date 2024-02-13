#!/usr/bin/node

const myArg = process.argv;
let mySum;
let myRealSum = 0;

function add (a, b) {
  mySum = Number(a) + Number(b);
  return (mySum);
}

myRealSum = add(myArg[2], myArg[3]);
console.log(myRealSum);
