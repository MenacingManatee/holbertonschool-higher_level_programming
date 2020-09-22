#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) { console.log(err); }
  const jsn = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < jsn.results.length; i++) {
    for (let j = 0; j < jsn.results[i].characters.length; j++) {
      if (jsn.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
