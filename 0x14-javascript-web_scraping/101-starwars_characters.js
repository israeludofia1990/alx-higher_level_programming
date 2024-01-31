#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Construct the URL for the Star Wars API films endpoint based on the provided movie ID
const url = 'https://swapi.co/api/films/' + process.argv[2];

// Make an HTTP request to the Star Wars API films endpoint
request(url, function (error, response, body) {
  // Check for errors during the request
  if (!error) {
    // Parse the response body as JSON and extract character URLs
    let characters = JSON.parse(body).characters;
    
    // Call the function to print characters
    printCharacters(characters, 0);
  }
});

// Recursive function to print characters
function printCharacters(characters, index) {
  // Make an HTTP request to each character URL
  request(characters[index], function (error, response, body) {
    // Check for errors during the request
    if (!error) {
      // Parse the response body as JSON and print the character's name
      console.log(JSON.parse(body).name);

      // If there are more characters, call the function recursively for the next character
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
