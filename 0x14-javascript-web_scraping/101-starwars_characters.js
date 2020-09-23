#!/usr/bin/node

const request = require('request');

let resObj = {}
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (err, res, body) {
    if (err) { console.log(err); }
    const jsn = JSON.parse(body);
    const chars = jsn.characters/*.sort(function sortChars (a, b) {
      const num1 = parseInt(a.slice(37, 39));
      const num2 = parseInt(b.slice(37, 39));
      if (num1 > num2) { return 1; } else if (num2 > num1) { return -1; } else { return 0; }
    });*/
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], function (err, res, body) {
        if (err) { console.log(err); }
        const jsn2 = JSON.parse(body);
        let tmp = {[parseInt(chars[i].slice(37, 39))]: jsn2.name}
        Object.assign(resObj, tmp)
//        resObj[parseInt(chars[i].slice(37, 39))] = jsn2.name;
//        for (const [key, val] of Object.entries(resObj)) {
//          console.log(val);
//        }
        console.log(i, resObj);
      });
    }
  console.log(resObj);
  }
);
