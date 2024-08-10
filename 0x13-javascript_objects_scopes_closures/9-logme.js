#!/usr/bin/node

let myCounter = 0;
exports.logMe = function (item) {
  console.log(`${myCounter}: ${item}`);
  myCounter++;
};
