#!/usr/bin/node

const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  charPrint (c) {
    let paint;
    if (c) {
      paint = c;
    } else {
      paint = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += paint;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
