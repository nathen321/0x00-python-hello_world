#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const [url, output] = process.argv.slice(2, 4);
request
  .get(url, function (err, msg, body) {
    if (err) return console.error(err);
    fs.writeFile(output, body, 'utf-8', function (err) {
      if (err) return console.error(err);
    });
  });
