#!/usr/bin/python3
"""
Defines ``matrix_divided()`` function.
"""


def matrix_divided(matrix, div):
    """Divides elements of ``matrix`` by ``div``

    ``matrix`` must be a list of lists of integers or floats,
    otherwise raise a ``TypeError`` exception.

    Each row of the ``matrix`` must be of the same size,
    otherwise raise a ``TypeError`` exception.

    ``div`` can't be equal to 0, otherwise raise a ``ZeroDivisionError``.

    All resulting elements should be rounded to 2 decimal places

    Args:
        matrix (:obj:list, None): list of lists of integers/floats
        div (int/float): divisior

    Returns:
        list: new matrix with the results

    Raises:
        TypeError: If the matrix type is not a list,
            its elements also not lists,
            and their elements are not int/float.
            If the size of rows in matrix aren't equal

        ZeroDivisionError: If ``div`` is 0
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg)

    new_matrix = []

    try:
        row_size = len(matrix[0])
    except TypeError:
        raise TypeError(msg)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)

        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        tmp = []
        for i in range(row_size):
            if type(row[i]) is not int and type(row[i]) is not float:
                raise TypeError(msg)

            if div == 0:
                raise ZeroDivisionError("division by zero")

            tmp.append(round(row[i] / div, 2))

        new_matrix.append(tmp)

    return new_matrix
