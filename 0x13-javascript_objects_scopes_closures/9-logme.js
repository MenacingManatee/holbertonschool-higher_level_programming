#!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  p = count++ + ': ' + item;
  console.log(p);
};
