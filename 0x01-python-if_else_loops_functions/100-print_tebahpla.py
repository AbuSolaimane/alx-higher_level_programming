#!/usr/bin/python3
changeFromUpperToLower = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - changeFromUpperToLower)), end="")
    changeFromUpperToLower = 32 if changeFromUpperToLower == 0 else 0
