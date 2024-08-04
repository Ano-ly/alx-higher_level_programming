#!/usr/bin/node

function addMeMaybe (digit, func) {
  func(digit + 1);
}

module.exports = { addMeMaybe };
