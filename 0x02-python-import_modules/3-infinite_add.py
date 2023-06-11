#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    numOfArgs = len(argv) - 1
    sum = 0

    if numOfArgs > 0:
        for i in range(numOfArgs):
            sum += int(argv[i + 1])

    print("{}".format(sum))
