#!/usr/bin/node

const prevsqr = require('./5-square');
module.exports = class Square extends prevsqr {
  charPrint (c) {
    let ch = c;
    if (c === undefined) {
      ch = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let p = '';
      for (let j = 0; j < this.width; j++) {
        p = p + ch;
      }
      console.log(p);
    }
  }
};
