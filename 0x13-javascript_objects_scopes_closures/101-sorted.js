#!/usr/bin/node

const dict = require('./101-data').dict;
const resDict = {};
for (const [key, val] of Object.entries(dict)) {
  let tmp;
  if (resDict[val] !== undefined) {
    tmp = resDict[val];
    tmp.push(key);
  } else {
    tmp = [key];
  }
  const tmp2 = { [val]: tmp };
  Object.assign(resDict, tmp2);
}
console.log(resDict);
