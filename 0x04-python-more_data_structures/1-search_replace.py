#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_new = list(map(lambda x: replace if x == search else x, my_list))
    #list_new = [replace for x in my_list if x == search, else x]
    return (list_new)
