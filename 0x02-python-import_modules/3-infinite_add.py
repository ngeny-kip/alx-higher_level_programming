#!/usr/bin/python3

if __name__ == "__main__":
    '''prints the addition of all arguments'''
    import sys

    count = 0

    for i in range(len(sys.argv) - 1):
        count += int(sys.argv[i + 1])
    print(f"{count}")
