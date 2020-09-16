#!/usr/bin/node

function fac(n1) {
  const n2 = n1;
  if (n1 === 1) {
    return 1
  } else if (n1 !== n2) {
    return 1
  } else {
    return n1 * fac(n1 - 1)
  }
}

const num = Math.trunc(Number(process.argv[2]));
const num2 = num;
if (num !== num2) {
  console.log('1');
} else {
  console.log(fac(num))
}
