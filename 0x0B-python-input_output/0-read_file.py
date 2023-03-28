#!/usr/bin/python3
<<<<<<< HEAD
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
=======
"""Mdoule Task 0"""


def read_file(filename=""):
    """To print the content of a text file."""
    with open(filename, 'r') as f:
        print(f.read(), end='')
>>>>>>> 03e68b8626e24a75ddeb4cf53d54125f51364ca6
