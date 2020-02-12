#!/usr/bin/env python3

def char_frequency(filename):
    """
    Counts the frequency of each character in the given file.
    """
    # First try to open the file
    try:
        f = open(filename)
    # code in the except block is only executed if one of the instructions in the try block raise an error of the matching type
    except OSError:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters