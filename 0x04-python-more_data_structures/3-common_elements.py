#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_common = [x for x in set_1 if x in set_1 and x in set_2]
    return (list_common)
