#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
# export FRUIT=Pineapple
print("FRUIT: " + os.environ.get("FRUIT", ""))