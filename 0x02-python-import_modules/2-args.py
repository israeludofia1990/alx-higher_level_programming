#!/usr/bin/python3

def print_arguments(argv):
    legnth = len(argv) - 1
    if legnth == 0:
        print("{:d} arguments.".format(legnth))
    elif legnth == 1:
        print("{:d} argument:".format(legnth))
        print("{:d}: {:s}".format(legnth, argv[1]))
    else:
        print("{:d} arguments:".format(legnth))
        i = 1
        while i <= legnth:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1


if __name__ == "__main__":
    import sys
    print_arguments(sys.argv)
