#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    l_copy = my_list.copy()
    l_copy.sort()
    return l_copy(-1)
