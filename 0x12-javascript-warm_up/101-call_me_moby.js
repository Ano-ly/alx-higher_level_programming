#!/usr/bin/node

function callMeMoby (rep, func) {
  for (let i = 0; i < rep; i++) {
    func();
  }
}

module.exports = { callMeMoby };
