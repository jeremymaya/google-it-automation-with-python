# Regular Expressions
log = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
index = log.index('[')

# Brittle way to extracing numbers by using index function
print(log[index+1:index+6])

# re module allows for search function to find regular expressions inside strings
import re
log = "July 31 7:51:48 mycomputer bad_process[12345]: ERROR Perfroming package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# Basic Regular Expressions
# Simple Matching in Python
# The "r" at the beginning of the pattern indicates that this is a rawstring
# Always use rawstrings for regular expressions in Python
result = re.search(r'aza', 'plaza')
print(result)

result = re.search(r'aza', 'bazaar')
print(result)

# None is a special value that Python uses that show that there's none actual value there
result = re.search(r'aza', 'maze')
print(result)


# The match attribute always has a value of the actual sub string that match the search pattern
# The span attribute indicates the range where the sub string can be found in the string
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "sponge"))

# Additional options to the search function can be added as a third parameter
# The re.IGNORECASE option returns a match that is case insensitive
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))