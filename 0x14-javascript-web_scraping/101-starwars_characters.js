#!/usr/bin/node

const request = require('request');

const resObj = {};
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (err, res, body) {
    if (err) { console.log(err); }
    const jsn = JSON.parse(body);
    const chars = jsn.characters;/* .sort(function sortChars (a, b) {
      const num1 = parseInt(a.slice(37, 39));
      const num2 = parseInt(b.slice(37, 39));
      if (num1 > num2) { return 1; } else if (num2 > num1) { return -1; } else { return 0; }
    }); */
    async function getNames () {
      for (let i = 0; i < chars.length; i++) {
        await request(chars[i], function (err, res, body) {
          if (err) { console.log(err); }
          const jsn2 = JSON.parse(body);
          const tmp = { [parseInt(chars[i].slice(37, 39))]: jsn2.name };
          Object.assign(resObj, tmp);
          if (i === chars.length - 1) {
            for (const val of Object.values(resObj)) {
              console.log(val);
            }
          }
        });
      }
    }
    getNames();
  }
);
