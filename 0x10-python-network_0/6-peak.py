#!/usr/bin/python3
"""
    look for the peak in a list
"""


def find_peak(list_of_integers):
    """
     this is a class
    """
    size = len(list_of_integers)
    mid = size
    midlle = size // 2

    if size == 0:
        return None

    while True:
        mid = mid // 2
        if (midlle < size - 1 and
                list_of_integers[midlle] < list_of_integers[midlle + 1]):
            if mid // 2 == 0:
                mid = 2
            midlle = midlle + mid // 2
        elif (mid > 0 and
                list_of_integers[midlle] < list_of_integers[midlle - 1]):
            if mid // 2 == 0:
                mid = 2
            midlle = midlle - mid // 2
        else:
            return list_of_integers[midlle]
