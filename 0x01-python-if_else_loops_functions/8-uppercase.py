#!/usr/bin/python3

# a function that print strings in uppercase followed by a new line
def uppercase(str):
    for i in str:
        i = ord(i)
        if 97 <= i <= 122:
            i = i - 32
        print("{:c}".format(i), end='')
    print()
