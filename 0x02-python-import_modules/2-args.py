#!/usr/bin/python3
#Prints the number of arguments received, and all the arguments
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l != 2:
        print("{} arguments".format(l - 1))
    else:
        print("1 argument")
        for i in range(l):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
