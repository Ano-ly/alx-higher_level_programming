#!/usr/bin/node

const fsMod = require('node:fs');
const myArgs = process.argv;
const filename = myArgs[2];
const content = myArgs[3];

fsMod.writeFile(filename, content, 'utf-8', (errorV, content) => {
  if (errorV) {
    console.error(errorV);
  }
});
