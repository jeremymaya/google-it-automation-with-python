# Expression and Variables
# Data Types
print(type("a"))
# <class 'str'>
print(type(2))
# <class 'int'>
print(type(2.5))
# <class 'float'>

# Variables - Calculate the area of a triangle of base 5, height 3 and output the result
base = 5
height = 3
area = (base * height) / 2

print(area)

# Expressions, Numbers, and Type Conversion
"""
In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Calculate the average file size by having Python add all the values for you, and then set the amount variable to the amount of files. Finally, output a message saying "The average size is: " followed by the resulting number.
"""
sum = 2048 + 4357 + 97658 + 125 + 8
amount = 5
average = sum/amount

print("The average size is: " + str(average))

# Functions
"""
Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
"""
def print_seconds(hours, minutes, seconds):
    print((hours * 60 * 60) + (minutes * 60) + seconds)

print_seconds(1,2,3)