#!/bin/bash
# sends a GET request to the URL, and displays the body
if [ "$(curl -ILs -w "%{http_code}" "$1")" == '200' ]; then
	curl -Ls "$1"
fi
