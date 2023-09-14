#!/usr/bin/python3
"""A JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.
    Args:
        filename (str): The name of the JSON file
    Returns:
        The object
    """
    with open(filename) as file:
        return json.load(file)
