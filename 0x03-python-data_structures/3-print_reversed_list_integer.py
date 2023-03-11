#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    copy = my_list.copy()
    copy.reverse()
    for i in copy:
        print("{:d}".format(i))
