#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_a = [x for x in set_1 if x not in set_2]
    set_b = [y for y in set_2 if y not in set_1]
    set_a.extend(set_b)
    return (set_a)
