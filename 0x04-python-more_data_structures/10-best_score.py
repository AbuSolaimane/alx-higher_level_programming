#!/usr/bin/python3
def best_score(a_dictionary):
    if len(list(a_dictionary)) == 0:
        return (None)
    max_key = list(a_dictionary.keys())[0]
    max_value = a_dictionary[max_key]
    for k, v in a_dictionary.items():
        if v > max_value:
            max_key = k
            max_value = v
    return (max_value)
best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10})
