#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or a_dictionary is None:
        return None
    dic_max = 0
    max_key = ""
    for key in a_dictionary.keys():
        if a_dictionary[key] > dic_max:
            dic_max = a_dictionary[key]
            max_key = key
    return (max_key)
