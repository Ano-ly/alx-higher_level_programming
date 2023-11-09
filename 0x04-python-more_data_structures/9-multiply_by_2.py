#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_new = {}
    for key in a_dictionary.keys():
        dic_new.update({key: (a_dictionary[key] * 2)})
    return (dic_new)
