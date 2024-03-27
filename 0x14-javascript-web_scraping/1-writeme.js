#!/usr/bin/node

const fsMod = require('node:fs');
const myArgs = process.argv;
const filename = myArgs[2];
const content = myArgs[3];

fsMod.writeFile(filename, '\ufeff' + content, (errorV, content) => {
  if (errorV) {
    console.error(errorV);
  }
});
