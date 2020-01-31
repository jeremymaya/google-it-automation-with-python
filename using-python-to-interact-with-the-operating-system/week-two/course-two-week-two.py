# Reading and Writing Files
# Creates a new file object and assigning it to a variable called file
# Current line assumes that the spider.txt file is in the same directory
file = open("using-python-to-interact-with-the-operating-system/week-two/spider.txt")

# readline method reads a single line of a file
print(file.readline())
# readline method reads the second line of a file - each time the readline method is called, the file object updates the current position in the file
print(file.readline())
# read method, which reads from the current position until the end of the file instead of just one line
print(file.read())

# Opened file needs to be closed to conform the open-close approach
file.close()

# "with" keyword creates a block of code with the work that needs to be done with the file inside of it
# When "with" block is used, Python will automatically close the file
with open("using-python-to-interact-with-the-operating-system/week-two/spider.txt") as file:
    print(file.readline())

# Iterates the file object like list or strings
# The file has a new line character at the end of each line
# When Python reads the file line by line, the line variable will always have a new line character at the end
with open("using-python-to-interact-with-the-operating-system/week-two/spider.txt") as file:
    for line in file:
        print(line.upper())

# Empty lines can be avoided by using strip method
with open("using-python-to-interact-with-the-operating-system/week-two/spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# Iterates the file object by reading the file lines into a list
file = open("using-python-to-interact-with-the-operating-system/week-two/spider.txt")
lines = file.readlines()
file.close
lines.sort()
print(lines)

# "with" block pattern takes the second argument which specifies in which mode the file should be opened as
with open("using-python-to-interact-with-the-operating-system/week-two/novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

# Managing Files and Directories
# os module provides a layer of abstraction between Python and the operating system
import os

# remove function deletes a file
os.remove("using-python-to-interact-with-the-operating-system/week-two/novel.txt")

# rename function renames a file
# The first parameter to rename function is the old name of the file and the second is new name
os.rename("using-python-to-interact-with-the-operating-system/week-two/spider.txt", "using-python-to-interact-with-the-operating-system/week-two/spider_rename.txt")
os.rename("using-python-to-interact-with-the-operating-system/week-two/spider_rename.txt", "using-python-to-interact-with-the-operating-system/week-two/spider.txt")

# the OS path sub-module's exists function checks whether a file exist
print(os.path.exists("using-python-to-interact-with-the-operating-system/week-two/spider_rename.txt"))