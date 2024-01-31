#!/usr/bin/node
const arg = require('process');
const fs = require('fs');

let path_to_file = arg.argv[2];
let text = arg.argv[3];

fs.writeFile(path_to_file, text, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  }
});
