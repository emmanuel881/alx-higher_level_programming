#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    leng = len(my_list)
    count = 1
    while(leng > 0):
        print("{:d}".format(my_list[(count * -1)]))
        leng = leng - 1
        count += 1
