#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or not isinstance(a_dictionary, dict):
        return (None)
    max_key = list(a_dictionary.keys())[0]
    max_value = a_dictionary[max_key]
    for k, v in a_dictionary.items():
        if v > max_value:
            max_key = k
            max_value = v
    return (max_value)
