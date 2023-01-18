#!/usr/bin/python3
import sys
if __name__ == "__main__":
    leng = len(sys.argv)
    if (leng <= 1):
        print("0 arguments.")
    else:
        i = 1
        if (leng == 2):
            print("{} argument:".format(leng - 1))
        else:
            print("{} arguments:".format(leng - 1))
        while (i <= (leng - 1)):
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
