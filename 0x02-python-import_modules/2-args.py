#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l == 1:
        print("0 arguments.")
    elif l == 2:
        print("1 argument:".format(l - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(l - 1))
        for i in range(1, l):
                print("{}: {}".format(i, sys.argv[i]))
