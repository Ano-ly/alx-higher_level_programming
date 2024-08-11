#!/usr/bin/node
const dict = require('./101-data.js').dict;
const lenList = new Set();
const finalObj = {};
for (const num in dict) {
  lenList.add(dict[num]);
}
for (const lens of lenList) {
  const nums = [];
  for (const [num, len] of Object.entries(dict)) {
    if (len === lens) {
      nums.push(num);
    }
  }
  finalObj[lens] = nums;
}
console.log(finalObj);
