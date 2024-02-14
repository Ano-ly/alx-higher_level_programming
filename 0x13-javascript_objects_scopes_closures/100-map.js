#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map(function (n) {
  return (n * list.indexOf(n));
});
console.log(list);
console.log(newList);
