#!/usr/bin/node

const req = require('request');
const myUrl = process.argv[2];

req.get(myUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const completedTasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 1;
      } else {
        completedTasks[todo.userId] += 1;
      }
    }
  });
  console.log(completedTasks);
});
