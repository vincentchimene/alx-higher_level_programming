#!/usr/bin/python3

# that converts a Roman numeral to an integer.
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    roman_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    for i in range(len(roman_string)):
        if roman_d.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                roman_d[roman_string[i]] < roman_d[roman_string[i + 1]]):
            number += roman_d[roman_string[i]] * -1
        else:
            number += roman_d[roman_string[i]]
    return (number)
