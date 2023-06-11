#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    numOfArgs = len(argv) - 1
    chaine = "argument" if numOfArgs == 1 else "arguments"
    print("{} {}".format(numOfArgs, chaine), end="")

    if numOfArgs > 0:
        print(":")
        for i in range(numOfArgs):
            print("{}: {}".format(i + 1, argv[i + 1]))
    else:
        print(".")
