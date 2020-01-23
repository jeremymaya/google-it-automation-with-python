# While Loops
# What is while loop and more examples
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1

print("x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)
# Why initializing variables matters
"""
In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?
"""
def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)