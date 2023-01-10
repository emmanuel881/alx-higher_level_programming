#!/usr/bin/python3
n = 0
j = 1
while n < 10:
    while j < 10:
        if (n == 8 and j == 9):
            print("{}{}".format(n, j))
        else:
            print("{}{}".format(n, j), end=", ")
        j = j + 1
    n = n + 1
    j = n + 1
