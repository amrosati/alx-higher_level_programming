#!/usr/bin/python3
"""Unittest for ``max_integer([..])``
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        self.n_list = [1, 2, 3, 4, 5]

    def test_maxInteger(self):
        self.assertEqual(max_integer(self.n_list), 5)

        self.n_list.append(5)
        self.assertEqual(max_integer(self.n_list), 5)
