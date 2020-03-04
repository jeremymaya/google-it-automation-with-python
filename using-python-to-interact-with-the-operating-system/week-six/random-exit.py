#!/usr/bin/env python

import sys
import random

# Uses random randint to generate a value between zero and three
value=random.randint(0, 3)
# Prints the selected value and exits with it
print("Returning: " + str(value))
sys.exit(value)