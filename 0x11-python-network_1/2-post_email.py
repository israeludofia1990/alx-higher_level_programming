#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as a parameter'''

if __name__ == "__main__":
    from sys import argv
    import urllib.parse
    import urllib.request

    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
