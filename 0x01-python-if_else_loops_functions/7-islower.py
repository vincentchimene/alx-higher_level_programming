#!/usr/bin/python3

# A function that checks for lowercase character.
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
