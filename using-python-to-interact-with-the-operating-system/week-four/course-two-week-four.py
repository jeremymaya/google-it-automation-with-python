
# Standard Streams
# STDIN - the standard input stream which is a channel between a program and a source of input
# STDOUT - the standard output stream which is a pathway between a program and a target of output
# SDTERR - the standard error stream which displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program
data = input("This comes from STDIN: ")
print("We are writing it to STDOUT: " + data)
# print("We are generating an error to STDERR: " + data + 1)

# -----------------------------------------------------------------------------------------

# Environment Variables
# os module provides environ dictionary
import os

# environ variables allows us to access environment variables
# get function specifies a default value when the key that we're looking for isn't in the dictionary
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))

# export FRUIT=Pineapple
print("FRUIT: " + os.environ.get("FRUIT", ""))

# -----------------------------------------------------------------------------------------

# Command-Line Arguments and Exit Status
import sys
print(sys.argv)

import os

# Receives a file name as a command line argument
# filename = sys.argv[0]

# Checks whether the file name exist or not
# When the file doesn't exist, it creates it by writing a line to it
# if not os.path.exists(filename):
#      with open(filename, "w") as f:
#          f.write("New file created\n")
# When the file exist, our script print an error message and exits with an exit value of one
# else:
#     print("Error, the file {} already exists!".format(filename))
#     sys.exit(1)

# =========================================================================================

# Python Subprocesses
# Running System Commands in Python
import subprocess
print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "2"]))

# -----------------------------------------------------------------------------------------

# Obtaining the Output of a System Command

# The "host" command converts a host name to an IP address and vice versa
# Stores the result in a variable by passing the capture_output=True so that the result can be accessed
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
# OUTPUT: b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
# b' indicates that the output is an array of bytes
print(result.stdout)
# Decode function applies an encoding to transform the bytes into a string
# It uses a UTF-8 encoding by default
print(result.stdout.decode().split())

# Executes the rm command to remove file that doesn't exist
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
# stdout prints empty value since there is an error 
print(result.stdout)
# stderr prints error value as the value can be accessed through the stderr attribute
print(result.stderr)

# -----------------------------------------------------------------------------------------

# Advanced Subprocess Management

# =========================================================================================