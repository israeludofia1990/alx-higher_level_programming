#!/usr/bin/node
const request = require('request');

// Get the URL from the command-line argument
const url = process.argv[2];

// Make an HTTP request
request(url, function (error, response, body) {
  // Check for errors during the request
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    // Parse the response body as JSON
    const data = JSON.parse(body);

    // Extract the results array from the response
    const results = data.results;

    // Count movies with a character whose URL ends with '/18/'
    const count = results.reduce((acc, movie) => {
      // Check if any character in the movie has a URL ending with '/18/'
      const hasCharacter18 = movie.characters.some((character) => character.endsWith('/18/'));

      // Increment the count if condition is met
      return hasCharacter18 ? acc + 1 : acc;
    }, 0);

    // Output the result
    console.log(count);
  } catch (parseError) {
    // Handle JSON parsing errors
    console.error('Error parsing JSON:', parseError.message);
  }
});
