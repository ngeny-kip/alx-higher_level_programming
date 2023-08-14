#!/usr/bin/python3

if _name_ == "_main_":
    '''prints sum, difference, multiple and qoutient'''
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print(f"{a} + {b} = {add(a,b)}")
    print(f"{a} + {b} = {sub(a,b)}")
    print(f"{a} + {b} = {div(a,b)}")
