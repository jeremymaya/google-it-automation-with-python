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
# Defining Functions
"""
Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
"""
def print_seconds(hours, minutes, seconds):
    print((hours * 60 * 60) + (minutes * 60) + seconds)

print_seconds(1,2,3)

# Returning Values
"""
Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.
"""
def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

# Example of returning multiple values from a function
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# The Principles of Code Reuse
"""
In this code, identify the repeated pattern and replace it with a function called print_monthly_expense, that receives the name of the month and the hours as parameters. Adapt the rest of the code so that the result is the same.
"""
june_hours = 243
june_cost = june_hours * 0.65
print("In June we spent: " + str(june_cost))

july_hours = 325
july_cost = july_hours * 0.65
print("In July we spent: " + str(july_cost))

august_hours = 298
august_cost = august_hours * 0.65
print("In August we spent: " + str(august_cost))

def print_monthly_expense(month, hours):
    print("In " + month + " we spent: " + str(hours * 0.65))

print_monthly_expense("June", 243)
print_monthly_expense("July", 325)
print_monthly_expense("August", 298)

# Coding Style
"""
This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6? Tip: a function that calculates the area of a rectangle should probably be called rectangle_area, and if it's receiving base and height, that's what the parameters should be called.
"""
def f1(x, y):
	z = x*y  # the area is base*height
	print("The area is " + str(z))

def rectangle_area(base, height):
    area = base*height
    print("The area is " + str(area))

rectangle_area(5, 6)

# Condtionals
# Equality Operators
print(10 > 1) # True
print("cat" == "dog") # False
print(1 != 2) # True
# print(1 < "1") # TypeError
print(1 == "1") # False
# Logical Operators
print("Yellow" > "Cyan" and "Brown" > "Magenta") # False
print(25 > 50 or 1 != 2) # True
print(not 42 == "Answer") # True

# Branching with if Statements
"""
The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?
"""
def is_positive(number):
    if number > 0:
        return True

# else Statements
"""
The is_positive function should return True if the number received is positive and False if it isn't. Can you fill in the gaps to make that happen?
"""
def is_positive_two(number):
    if number > 0:
        return True
    else:
        return False


# elif Statements
"""
The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?
"""
def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative