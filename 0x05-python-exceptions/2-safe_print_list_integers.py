#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for el in my_list:
        if (n == x):
            break
        try:
            n += 1
            print("{:d}".format(el), end="")
        except ValueError:
            n -= 1
            continue
    print()
    try:
        return n
    except UnboundLocalError:
        return 0
