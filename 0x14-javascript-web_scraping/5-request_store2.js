#!/usr/bin/node

const requestMod = require('request');
const fsMod = require('node:fs');
const myArgs = process.argv;
const url = myArgs[2];
const filePath = myArgs[3];

requestMod.get(url, function (errorV, response) {
  if (errorV) {
    console.error(errorV);
  }
  console.log(JSON.stringify(response))
  fsMod.writeFile(filePath, response, 'utf-8', (errorV, content) => {
    if (errorV) {
      console.error(errorV);
    }
  });
});

