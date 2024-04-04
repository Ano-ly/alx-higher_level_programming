#!/usr/bin/node

const requestMod = require('request');
const myArgs = process.argv;
const url = myArgs[2]

requestMod.get(url, function (errorV, content) {
  if (errorV) {
    console.error(errorV);
  }
  const myList = JSON.parse(content);
  let count = myList.length;
  let displayDict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0,
                     '8': 0, '9': 0, '10': 0};
  for (let j=0; j<count; i++) {
    userId = String(myList[j].userId);
    if (displayDict.hasOwnProperty(userId)) {
      displayDict[userId]++;
    }
  }
  console.log(displayDict);
});
