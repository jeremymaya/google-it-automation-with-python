# Crash Course of Python - Week 3

## Learning Objectives
* Understand the role and value of loops
* Understand the differences between while and for loops
* Write code that uses while and for loops
* Understand recursion and why it may be useful in scripting

---

## While Loops
### What is a while loop?
While Loops instruct computer to continuously execute the code based on the value of a condition. The difference between if statements and while loop is that the body of the block can be executed multiple times instead of just once.

**Initialization** is to give an initial value to a variable.

### Why initializing variables matters
When we forget to initialize the variable two different things can happen:
1. A name error when we forget to initialize a variable 
2. When we forget to initialize variables with the right value

### Infinite loops and how to break them
While loops:
* Use the condition to check when to exit
* The body of the while loop needs to make sure that the condition being checked will change

An **infinite loop**, a loop that keeps executing and never stops.

**Break** keyword can stop infinite loops but also to stop a loop early if the code has already achieved what's needed.

---

## for Loops
### What is for loop?
For loops iterate over a sequence of values. The for loop can iterate over a sequence of values of any type, not just a range of numbers.

The range function, range():
1. A range of numbers will start with the value 0 by default.
2. The list of numbers generated will be one less than the given value
3. The range function takes two parameters to the function instead of one to specify the first element of the list to generate
4. The range function takes a third parameter to change the size of each step (increments)

### Nested for Loops
**Nested for loops** are two for loops, one inside the other.

However, use caution when using nested for loops since the longer the list your code needs to iterate through, the longer it takes computer to complete the task. 

### Common Errors
The interpreter will refuse to iterate over a single element. This can be mitigated by:
1. Using range()
2. Make the loop iterate over a list with the single element

Since strings are iterable, above solution may be needed. 

for loops are best when you want to iterate over a known sequence of elements but when you want to operate while a certain condition is true, while loops are the best choice.

---

## Recursion
### What is recursion?
**Recursion** is the repeated application of the same procedure to a smaller problem. It tackles complex problems by reducing the problem to a simpler one by a function call itself until it reaches the **base case**.

In Python, a recursive function can be called up to 1,000 times.

---


## Credit
* [Coursera - Python Crash Course Week 3](https://www.coursera.org/learn/python-crash-course/home/week/3)