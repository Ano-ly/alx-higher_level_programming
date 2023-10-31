#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = number
if number < 0:
    number1 = -number
last_digit = number1 % 10
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
if (last_digit < 6) and (last_digit != 0):
    print("Last digit of", number, "is", last_digit, "and is less than 6 and \
not 0")
if last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
