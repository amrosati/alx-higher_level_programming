#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq = []

    for item in my_list:
        if item not in uniq:
            uniq.append(item)
    for x in uniq:
        result += x

    return result
