#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_uniq = set(my_list)
    sum = 0
    for item in list_uniq:
        sum += item
    return (sum)
