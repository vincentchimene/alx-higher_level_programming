#!/usr/bin/python3

"""A program that prints the number of and the list of its arguments.
The output should be:
Number of argument(s) followed by argument (if number is one)
or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :,
followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet,
but imagine that argv can be used just like a C array:
you can use an index to walk through it.
There are other ways (which will be preferred for future project tasks), if you know them you can use them.
"""
if __name__ == "__main__":
    from sys import argv
    print("{}".format(len(argv) - 1), end=' argument' if len(argv) == 2
          else ' arguments')
    print("", end='.\n' if len(argv) == 1 else ':\n')
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
