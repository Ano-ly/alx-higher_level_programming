#!/usr/bin/node

const lenn = process.argv.length;

if (lenn === 2) {
  console.log('No argument');
} else if (lenn === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
