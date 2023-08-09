#!/usr/bin/python3

# A function that prints the last digit of a number
def print_last_digit(number):
        number = abs(number) % 10
        print(number, end="")
        return number
