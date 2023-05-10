#!/usr/bin/python3

"""``is_same_class`` function definition
"""


def is_same_class(obj, a_class):
    """Checks if ``obj`` is an instance of ``a_class``

    Args:
        obj (::obj::): Any object
        a_class (::obj::): class

    Returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise
    """
    if isinstance(a_class, type):
        return isinstance(obj, a_class)

    return isinstance(obj, eval(a_class))
