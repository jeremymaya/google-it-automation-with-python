# Strings
# What is a string?
"""
Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.
"""
def double_word(word):
    word *= 2
    count = 0
    for letter in word:
      count += 1
    return word + str(count)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
# The Parts of a String
"""
Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
"""
def first_and_last(message):
    if message == "" or message[0] == message[-1]:
      return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# Creating New Strings
"""
Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".
"""
word = "supercalifragilisticexpialidocious"
print(word.index("x"))

# More String Methods
"""
Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
"""
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# Formatting Strings
"""
Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
"""
def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))