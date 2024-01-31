#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API films endpoint
const apiUrl = `http://swapi.co/api/films/${movieId}`;

// Make an HTTP request to the Star Wars API films endpoint
request(apiUrl, function (error, response, body) {
  // Check for errors during the request
  if (error) {
    console.error(error); // Print the error if one occurred
    return;
  }

  try {
    const data = JSON.parse(body);

    // Check if the response contains an error message
    if (data.detail && data.detail.includes("Endpoint not meant for programmatic use.")) {
      console.error('API error:', data.detail);
      return;
    }

    // Check if the movie title exists in the response
    if (data.title) {
      console.log(data.title);
    } else {
      console.error('Unexpected response format. Unable to retrieve movie title.');
    }
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
