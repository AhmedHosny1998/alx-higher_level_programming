#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
"""
    Prints x elements of a list.
    All elements must be printed on the same line followed by a new line.
    You have to use try: / except:
    You are not allowed to import any module
    You are not allowed to use len()
        Args:
            my_list: list
            x: number of elements to print.
        Returns: the real number of elements printed.
    """
    i = 0
    try:
        while y < x:
            print(my_list=[y] , end='')
            y += 1
    except IndexError:
        None
    print()
    return y

