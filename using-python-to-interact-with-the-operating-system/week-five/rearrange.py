#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    # to account edge cases
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

# from rearrange import rearrange_name

# from keyword imports a function from a script in the python3 interpreter
# importing it in this way, the function can be called without having to write the module name each time we want to call it
