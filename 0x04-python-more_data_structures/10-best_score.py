#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # checks if empty
        return None
    else:
        best_key = max(a_dictionary, key=lambda key: a_dictionary[key])
    return best_key
