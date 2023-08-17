#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ordered_key = list(a_dictionary.keys())
    ordered_key.sort()

    for i in ordered_key:
        prnt(f"{i}:{a_dictionary.get(i)}")
