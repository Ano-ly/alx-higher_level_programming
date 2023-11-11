#!/usr/bin/python3
def uppercase(str):
    letter_upper = 0
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter_upper = ord(letter) - 32
        else:
            letter_upper = ord(letter)
        print("{}".format(chr(letter_upper)), end="")
        print("\n", end="")
