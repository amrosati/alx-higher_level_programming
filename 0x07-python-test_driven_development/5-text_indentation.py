#!/usr/bin/python3
"""
Defines a function tha prints a text with 2 new lines
after each of these characters: ``.``, ``?`` and ``:``.
"""


def text_indentation(text):
    """Indents text with new lines

    Prints two new lines after each of the following characters:
    ``.``, ``?`` and ``:``.

    There should be no space at the beginning or at the end
    of each printed line.

    Args:
        text (::obj::str): String to be indented

    Raises:
        TypeError: If ``text`` is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flags = ".?:"

    for char in text:
        print(char, end="")

        if char in flags:
            print("\n")
