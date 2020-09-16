#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = [Math.trunc(Number(process.argv[2])), 0];
  let i;
  for (i = 3; i < process.argv.length; i++) {
    if (Math.trunc(Number(process.argv[i])) >= arr[0]) {
      arr[1] = arr[0];
      arr[0] = Math.trunc(Number(process.argv[i]));
    } else if (Math.trunc(Number(process.argv[i])) >= arr[1]) {
      arr[1] = Math.trunc(Number(process.argv[i]));
    }
  }
  console.log(arr[1]);
}
