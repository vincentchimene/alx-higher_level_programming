#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    split_text_list = list()
    new_text = list()
    letters_list = list()

    for character in text:
        letters_list.append(character)
        if character in ['.', '?', ':']:
            split_text_list.append(''.join(letters_list))
            letters_list.clear()

    if letters_list:
        split_text_list.append("".join(letters_list))
    letters_list.clear()

    for sentence in split_text_list:
        new_text.append(sentence.strip(' '))
    split_text_list.clear()

    for character in new_text[-1]:
        if character in ['.', '?', ':']:
            print("\n\n".join(new_text))
            print()
            return

    print("\n\n".join(new_text), end='')
