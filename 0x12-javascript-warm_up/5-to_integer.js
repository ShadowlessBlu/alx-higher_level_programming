#!/usr/bin/node

const arg1 = process.argv[2];
const n = parseInt(arg1, 10);

if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${n}`);
}