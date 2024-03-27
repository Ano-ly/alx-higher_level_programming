#!/usr/bin/node

const requestMod = require('request');
const myArgs = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films';
const idEps = myArgs[2];

requestMod.get(url, function (errorV, response, content) {
  if (errorV) {
    console.error(errorV);
  }
  const myDict = JSON.parse(content);
  const noEps = myDict.count;
  const eps = myDict.results;
  for (let i = 0; i < noEps; i++) {
    if (eps[i].episode_id === Number(idEps)) {
      console.log(eps[i].title);
    }
  }
});
