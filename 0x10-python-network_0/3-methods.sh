#!/bin/bash
# Options request on the server
curl -sI -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
