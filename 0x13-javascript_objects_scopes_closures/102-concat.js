#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.appendFile(args[4], args[2], function (err) {
  if (err) {
    throw err;
  }
});
fs.appendFile(args[4], args[3], function (err) {
  if (err) {
    throw err;
  }
});
