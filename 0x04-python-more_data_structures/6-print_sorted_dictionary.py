#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for item in sorted(list(a_dictionary)):
        print("{}: {}".format(item, a_dictionary[item]))
