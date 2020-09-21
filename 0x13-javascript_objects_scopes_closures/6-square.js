#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let p = '';
      for (let j = 0; j < this.width; j++) {
        p = p + c;
      }
      console.log(p);
    }
  }
};
