#!/usr/bin/node

const fs = require('fs')

let file1;
let file2;
let tmp = fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    file1 = '';
  }
  else {
    file1 = data;
  }
  fs.writeFile(process.argv[4], file1, function (err) {
    if (err) throw err;
    });
});
fs.readFile(process.argv[3], 'utf-8', (err, data) => {
  if (err) {
    file2 = '';
  }
  else {
    file2 = data;
  }
  fs.appendFile(process.argv[4], file2, function (err) {
    if (err) throw err;
  });
});
