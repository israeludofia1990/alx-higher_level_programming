#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const todos = JSON.parse(body);

    if (!Array.isArray(todos)) {
      console.error('Unexpected response format. Expected an array.');
      return;
    }

    let completed = {};

    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });

    console.log(completed);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});

