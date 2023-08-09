#!/usr/bin/python3

# Write a function that creates a copy of the string,
# removing the character at the position n
# (not the Python way, the “C array index”).
def remove_char_at(str, n):
    if n >= 0:
        return (str[:n] + str[n + 1:])
    else:
        return (str)
