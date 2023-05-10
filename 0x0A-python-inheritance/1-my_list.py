#!/usr/bin/python3

"""``MyList`` class
"""


class MyList(list):
    """Inherits from ``list`` class
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending order)
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
