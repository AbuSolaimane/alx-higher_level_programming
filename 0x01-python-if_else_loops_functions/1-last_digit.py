#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
if number < 0:
    last_number = -1 * last_number
print(f"Last digit of {number} is {last_number} ", end="")
if last_number > 5:
    print(f"and is greater than 5")
elif last_number == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")