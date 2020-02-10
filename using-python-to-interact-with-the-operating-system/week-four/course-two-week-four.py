
# Standard Streams
# STDIN - the standard input stream which is a channel between a program and a source of input
# STDOUT - the standard output stream which is a pathway between a program and a target of output
# SDTERR - the standard error stream which displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program
data = input("This comes from STDIN: ")
print("We are writing it to STDOUT: " + data)
print("We are generating an error to STDERR: " + data + 1)

# -----------------------------------------------------------------------------------------