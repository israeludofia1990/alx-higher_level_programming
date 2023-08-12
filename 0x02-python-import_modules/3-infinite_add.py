#!/usr/bin/python3
def add_args(argv):
    length = len(argv) - 1
    if length == 0:
        return (0)
    elif length == 1:
        add = int(argv[1])
        return (add)
    else:
        add = 0
        i = 1
        while i <= length:
            add += int(argv[i])
            i += 1
        return (add)


if __name__ == "__main__":
    import sys
    total_sum = add_args(sys.argv)
    print("{:d}".format(total_sum))
