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

# =========================================================================================

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

# -----------------------------------------------------------------------------------------

# Wildcards and Character Classes
# Character classes are written inside square brackets
# It list the characters to match inside of the brackets
# A range of characters can be defined using a dash
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

# Use a ^, circumflex, inside the square brackets to match any characters that aren't in a group
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# Use a |, pipe symbol to match either one expression or another
# The search function returns the first matching string only when there are multiple matches
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))

# Use the findall function provided by the re module to get all possible matches
print(re.findall(r"cat|dog", "I like both cats and dogs."))

# -----------------------------------------------------------------------------------------

# Repetition Qualifiers
# Repeated matches is a common expressions that include a . followed by a *
# It matches any character repeated as many times as possible including zero - greedy behavior
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py.*n", "Pyn"))

# Use a +, plus character, to match one or more occurrences of the character that comes before it
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# Use a ?, question mark symbol, for either zero or one occurrence of the character before it
# It is used to specified optional characters
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

# -----------------------------------------------------------------------------------------

# Escaping Characters
# A pattern that includes a \ could be escaping a special regex character or a special string character
# Use a \, escape character, to match one of the special characters
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

# Use \w to match any alphanumeric character including letters, numbers, and underscores
# Use \d to match digits
# Use \s for matching whitespace characters like space, tab or new line
# Use \b for word boundaries
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# -----------------------------------------------------------------------------------------

# Regular Expressions in Action
# "Azerbaijan" returns "Azerbaija" because we did not specify the end 
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))

# "Azerbaijan" returns None 
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-Z0-9_]*$"
print(re.search(pattern, "this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable name"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

# =========================================================================================

# Advanced Regular Expressions
# Capturing Groups
# Use parentheses to capture groups which are portions of the pattern that are enclosed in
# Below line defines two separate groups
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

# The group method returns a tuple of two elements
print(result.groups())

# Use indexing to access these groups
# The first element contains the text matched by the entire regular expression
# Each successive element contains the data that was matched by every subsequent match group
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return print(name)
    return print("{} {}".format(result[2], result[1]))

rearrange_name("Lovelace, Ada")
rearrange_name("Ritchie, Dennis")
rearrange_name("Hopper, Grace M.")

def rearrange_name_updated(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return print(name)
    return print("{} {}".format(result[2], result[1]))

rearrange_name_updated("Hopper, Grace M.")

# -----------------------------------------------------------------------------------------

# More on Repetition Qualifiers
# Use {}, curly brackets and one or two numbers to specify a range with numeric repetition qualifiers
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# Use \b, which matches word limits at the beginning and end of the pattern, to match full words 
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))

# -----------------------------------------------------------------------------------------

# Extracting a PID Using regexes in Python
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

# Trying to access the index 1. Therefore returs None
# result = re.search(regex, "99 elephants in a [cage]")
# print(result[1])

def extract_pid(log_line):
    regex = r"\[(\d+)]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

# -----------------------------------------------------------------------------------------

# Splitting and Replacing
# Split function from the re module works by taking any regular expression as a separator
# Use capturing parentheses to split list to include the elements that is used to split tje values
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

# Sub function from the re module is used for creating new strings by substituting all or part of them for a different string
# It uses regular expressions for both the matching and the replacing
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))