# Introduction to Python
# What is Python - Let's make friends!
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

# Other Languages - Prints "Hello, World!" 10 times
# Notice the similarities and differences between different scripting languages
"""
Bash: 
for i in {1...10}; do
    echo Hello, World

PowerShell:
for ($i; $i -le 10; $i++) {
    Write-Host "Hello, World!"
}
"""
for i in range(10):
    print("Hello, World!")

# Pratice Quiz- Fill in the correct Python comman to put "My first Python program" onto the screen.
print("My first Python program")

# Hello World
# Hello, World! - Write a Python script that outputs "I'm programming in Python!"
print("I'm programming in Python!")

# Getting Information from the User - Change the values of color and thing to have the computer output a different statement than the initial one
name = "Green"
thing = "Hope"
print(name + " is the color of " + thing)

name = "Blue"
thing = "Sky"
print(name + " is the color of " + thing)

# Python Can Be Your Calculator
# Addtion = 9
print(4+5)
# Multiplication = 63
print (9*7)
# Division = -0.25
print(-1/4)
# Division - Repeating or periodic numbers = 0.3333333333333333
print(1/3)
# Order of operations (PEMDAS)
print(((2050/5)-32)/9)
# 2 to the power of 10
print(2**10)
# Use Python to calcualte (((1 + 2) * 3) / 4)^5
print((((1+2)*3)/4)**5)

# Practice Quiz - Calculate the Golden ratio
ratio = ((1+(5**(1/2)))/2)
print(ratio)