#!/usr/bin/node

const requestMod = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

requestMod.get(url, function (errorV, response, content) {
  if (errorV) {
    console.error(errorV);
  }
  const myDict = JSON.parse(content);
  const seeList = myDict.results;
  const titleList = [];
  for (const movie of seeList) {
    titleList.push(movie.title);
  }
  for (const title of titleList) {
    $('UL#list_movies').append($('<li></li>').text(title));
  }
});
