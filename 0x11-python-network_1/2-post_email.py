#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as a parameter'''
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
