#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request
  .get(url, function (err, response, body) {
    if (err) return console.error(err);
    const tasks = JSON.parse(body);
    const dict = {};
    let userId;
    let completed;
    for (const index in tasks) {
      userId = tasks[index].userId;
      completed = tasks[index].completed;
      if (completed) {
        if (!dict[userId]) dict[userId] = 0;
        dict[userId] += 1;
      }
    }
    console.log(dict);
  });
