#!/usr/bin/python3
"""The write_file function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file.
        Args:
            filename (str): name of file.
            text (str): text to be written.
        Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as files:
        return files.write(text)
