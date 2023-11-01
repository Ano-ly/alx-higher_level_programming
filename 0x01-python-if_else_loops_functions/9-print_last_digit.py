#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    num_last = number % 10
    print("{}".format(num_last), end="")
    return (num_last)
