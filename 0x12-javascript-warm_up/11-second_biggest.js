#!/usr/bin/node

let len = 0;
const myArg = process.argv;
let x = 0;

myArg.forEach((val, index) => {
  len++;
});

if (len === 2 || len === 3) {
  console.log(0);
} else {
  x = Number(myArg[2]);
  myArg.forEach((val, index) => {
    if (Number(val) > x) {
      x = Number(val);
    }
  });
  let y = 0;
  myArg.forEach((val, index) => {
    if (Number(val) < x) {
      y = Number(val);
    }
  });
  myArg.forEach((val, index) => {
    if ((Number(val) > y) && (Number(val) !== x)) {
      y = Number(val);
    }
  });

  console.log(y);
}
