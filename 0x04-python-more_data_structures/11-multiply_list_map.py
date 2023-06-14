#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied by a number"""
    return (list(map(lambda x: x*number, my_list)))
