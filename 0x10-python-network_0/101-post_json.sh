#!/bin/bash
# post request with json data
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
