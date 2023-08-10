#!/usr/bin/python3
for c in range(97, 123):
    if chr(c) is not 'q' and chr(c) is not 'e':
        print("{}".format(chr(c)), end="")
