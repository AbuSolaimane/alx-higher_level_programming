#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    mySum = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end="")
            mySum += 1
        except Exception:
            break
    print("")
    return (mySum)
