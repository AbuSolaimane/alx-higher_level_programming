#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    my_average = 0
    my_div = 0
    for tupl in my_list:
        my_average += tupl[0] * tupl[1]
        my_div += tupl[1]
    return float(my_average / my_div)
