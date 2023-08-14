#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''prints all integer of a list in reverse order'''
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
