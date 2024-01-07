#!/usr/bin/python3
''' displays the value of the X-Request-Id variable '''


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()
        headers = response.getheader('X-Request-Id')
    print(headers)
