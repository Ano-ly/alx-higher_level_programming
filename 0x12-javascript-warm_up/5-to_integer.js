#!/usr/bin/node

const myArg = process.argv;

const inInt = Number(myArg[2]);

if (!isNaN(inInt)) {
  console.log('My number: ' + inInt);
} else {
  console.log('Not a number');
}
