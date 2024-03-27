#!/usr/bin/node

const fsMod = require('node:fs');
const myArgs = process.argv;
const filename = myArgs[2];
fsMod.readFile(filename, 'utf8', (errorV, content) => {
  if (errorV) {
    console.error(errorV);
    return;
  }
  console.log(content);
});
