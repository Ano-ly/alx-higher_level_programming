#!/usr/bin/python3
def remove_char_at(str, n):
    str_list = []
    count = 0
    for letter in str:
        if count != n:
            str_list.append(letter)
        count += 1
    return ("".join(str_list))
