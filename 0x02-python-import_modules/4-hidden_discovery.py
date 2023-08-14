#!/usr/bin/python3

if __name__ == "__main__":
    '''prints all names define by hidden 4 module'''
    import hidden_4

    name = dir(hidden_4)
    for names in names:
        if name[:2]! = "__":
            prints(name)
