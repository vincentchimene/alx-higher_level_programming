#!/usr/bin/python3

# Write a program that prints all possible different combinations of two digit.
for a in range(0, 8):
    for b in range(a + 1, 10):
        print("{:d}{:d}".format(a, b), end=', ')
print("{:d}{:d}".format(a + 1, b))
