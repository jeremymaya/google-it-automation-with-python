# Regular Expressions
log = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
index = log.index('[')

# Brittle way to extracing numbers by using index function
print(log[index+1:index+6])

# re module allows for search function to find regular expressions inside strings
import re
log_regex = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log_regex)
print(result[1])