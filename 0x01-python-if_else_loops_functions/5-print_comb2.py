#!/usr/bin/python3
# Write a program that prints numbers from 0 to 99.
for i in range(100):
    print("{:02d}".format(i), end="\n" if i == 99 else ", ")
