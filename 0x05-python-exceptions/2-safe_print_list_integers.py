#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(el), end="")
            n += 1
        except (ValueError, TypeError):
            n -= 1
            continue
    print()
    return n
