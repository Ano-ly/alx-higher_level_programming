#!/usr/bin/node

const requestMod = require('request');
const myArgs = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/3';
const idEps = myArgs[2];

requestMod.get(url, function (errorV, response, content) {
  if (errorV) {
    console.error(errorV);
  }
  const myDict = JSON.parse(content);
  console.log(myDict)
});
