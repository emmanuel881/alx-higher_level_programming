#!/usr/bin/python3
i = 97
for i in range(97, 123):
    if (i == 101 or i == 113):
        continue
    else:
        print("{:c}".format(i), end="")
