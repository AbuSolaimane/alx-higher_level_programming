#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for integer in my_list:
            print("{:d}".format(integer))
print_reversed_list_integer([1, 3, 4])