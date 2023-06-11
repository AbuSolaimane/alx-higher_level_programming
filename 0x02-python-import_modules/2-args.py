#!/usr/bin/python3

if __name__ == "__main__":
    numOfArgs = len(argv)
    chaine = numOfArgs == 1 ? "argument" : "arguments"
    print("{} {}".format(numOfArgs, chaine), end="")

    if numOfArgs > 0:
        print(":")
        for i in range(numOfArgs):
            print("{}: {}".format(i + 1, argv[i]))
    else:
        print(".")

