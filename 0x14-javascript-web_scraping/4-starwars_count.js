#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (
  err, response, body) {
  if (err) {
    console.log(err);
  }
  const jsn = JSON.parse(body);
  console.log(jsn.title);
}
);
