#!/usr/bin/node

const num1 = Math.trunc(Number(process.argv[2]));
const num2 = num1;
if (num1 !== num2) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < num1; i++) {
    console.log('C is fun');
  }
}
