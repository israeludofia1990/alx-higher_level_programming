#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `http://swapi.co/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    if (data.title) {
      console.log(data.title);
    } else {
      console.error('Unexpected response format. Unable to retrieve movie title.');
    }
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
