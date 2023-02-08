#!/usr/bin/python3
def search_replace(my_list, search, replace):
    leng = len(my_list)
    copy = []
    for i in range(leng):
        if (my_list[i] == search):
            copy.append(replace)
        else:
            copy.append(my_list[i])
    return copy
