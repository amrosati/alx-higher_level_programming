#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    name = None

    for key in a_dictionary:
        if a_dictionary[key] > score:
            score = a_dictionary[key]
            name = key

    return name
