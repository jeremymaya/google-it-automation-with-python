#!/usr/bin/env python3

# Writing Unit Tests in Python
# from keyword imports a function from a script in the python3 interpreter
# the function can be called without having to write the module name each time we want to call it
from rearrange import rearrange_name
# unittest module includes classes and methods for creating unit tests
import unittest

# Include the class that we want to inherit from in the parentheses
# TestRearrange class inherits from TestCase
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

# Runs the test
unittest.main()