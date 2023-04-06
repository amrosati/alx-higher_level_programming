#!/usr/bin/python3
import sys

x = sys.argv[1]
l = ['a', 'b', 'c']

if x not in l:
    print(x)
else:
    print(l)
