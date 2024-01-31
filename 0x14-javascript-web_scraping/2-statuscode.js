#!/usr/bin/node
const arg = require('process');
const req_mod = require('request');

let url = arg.argv[2];

req_mod(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
