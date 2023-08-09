#!/usr/bin/python3

# Write a program that prints the ASCII alphabet,
# in reverse order, alternating lowercase and uppercase
# (z in lowercase and Y in uppercase) , not followed by a new line.
for a in range(122, 96, -1):
    if a % 2 == 1:
        a -= 32
    print("{:c}".format(a), end="")
