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

# Infinite loops and how to break them
"""
The following code contains a mistake that can trigger an infinite loop, can you figure out how to fix it?
"""
def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n += 1

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3
