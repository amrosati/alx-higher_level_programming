#!/usr/bin/python3
"""
Defines printing a full name function
"""


def say_my_name(first_name, last_name=""):
    """Prints full name to stdout

    Prints in the format "My name is ``first_name`` ``last_name``"

    Args:
        first_name (str): first name
        last_name (str): last name

    Returns:
        nothing

    Raises:
        TypeError: If ``first_name`` of ``last_name`` are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {}".format(first_name), end="")
    if not last_name:
        print()
    else:
        print(" {}".format(last_name))
