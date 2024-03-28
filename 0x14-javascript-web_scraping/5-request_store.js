#!/usr/bin/node

const requestMod = require('request');
const fsMod = require('node:fs');
const myArgs = process.argv;
const url = myArgs[2];
const filePath = myArgs[3];

requestMod
  .get(url)
  .on('errorV', function (errorV) {
    console.error(errorV);
  })
  .pipe(fsMod.createWriteStream(filePath, { encoding: 'utf-8' }));
