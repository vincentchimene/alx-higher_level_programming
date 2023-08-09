#!/usr/bin/python3

# a function that prints numbers 1 - 100
# but replaces multiples of 3 with fizz,
# multiples of 5 with buzz and those of 15 with fizzbuzz
def fizzbuzz():
    for i in range(1, 101):
        if (i % 15) == 0:
            print("FizzBuzz", end=" ")
        elif (i % 3) == 0:
            print("Fizz", end=" ")
        elif (i % 5) == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
