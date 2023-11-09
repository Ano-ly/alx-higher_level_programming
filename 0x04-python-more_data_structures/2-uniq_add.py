#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_new_list = list(set(my_list))
    add_val = 0
    for i in my_new_list:
        add_val += i
    return (add_val)
