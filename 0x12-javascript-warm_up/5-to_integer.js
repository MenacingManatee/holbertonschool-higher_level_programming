#!/usr/bin/node

const num = Math.trunc(Number(process.argv[2]));
const num2 = num;
if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (num !== num2) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
