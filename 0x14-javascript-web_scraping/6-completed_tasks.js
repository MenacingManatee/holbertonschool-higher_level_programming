#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) { console.log(err); }
  const jsn = JSON.parse(body);
  let resObj = {};
  for (obj in jsn) {
    if (jsn[obj].completed) {
      if (resObj[jsn[obj].userId]) {
        resObj[jsn[obj].userId] += 1;
      }
      else {
        resObj[jsn[obj].userId] = 1;
      }
    }
  }
  console.log(resObj);
});
