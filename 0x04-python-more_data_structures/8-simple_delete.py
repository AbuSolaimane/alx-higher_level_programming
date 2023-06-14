#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    my_a_dictionary = a_dictionary
    if key in a_dictionary.keys():
        del my_a_dictionary[key]
    return (my_a_dictionary)
