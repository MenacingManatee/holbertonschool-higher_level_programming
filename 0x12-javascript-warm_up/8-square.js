#!/usr/bin/node

const num1 = Math.trunc(Number(process.argv[2]));
const num2 = num1;
if (num1 !== num2) {
  console.log('Missing size');
} else {
  let i;
  let j;
  let str = '';
  for (i = 0; i < num1; i++) {
    for (j = 0; j < num1; j++) {
      str = str + '#';
    }
    console.log(str);
    str = '';
  }
}
