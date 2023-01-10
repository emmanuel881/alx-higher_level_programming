#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            b = ord(i)
            upify = (b - 97) + 65
            upper = chr(upify)
            i = upper
        print("{}".format(i), end="")
    print("\n")
