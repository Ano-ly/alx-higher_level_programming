#!/usr/bin/node

const requestMod = require('request');
const myArgs = process.argv;
const url = myArgs[2]

requestMod.get(url, function (errorV, content) {
  if (errorV) {
    console.error(errorV);
  }
  console.log(content)
});
