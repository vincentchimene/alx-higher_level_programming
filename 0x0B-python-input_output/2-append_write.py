#!/usr/bin/python3
"""A function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): To be appended file
        text (str): String to append to the file.
    Returns:
        Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
