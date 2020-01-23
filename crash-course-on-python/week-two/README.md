# Crash Course of Python - Week 2

## Learning Objectives
* Write scripts that use variables of different data types
* Understand how flow control works in Python
* Implement branches with conditional expressions
* Encapsulate code into functions

---

## Expression and Variables
### Data Types
There are different data tpyes in Python. Some of the examples include:
* String which represents text wrapped in quotation marks to be manipulated by a script
* Integer which represents whole numbers without a fraction (ex. 1)
* Float which represents real numbers like a number with a fractional part (ex. 2.5)

Generally, computer doesn't know how to mix different data types - it results "TypeError".

If you're ever not 100 percent sure what data types a certain value is, Python gives you a handy way to find out. You can use the type function, to have the computer tell you the type

### Variables
* **Variables** are names that we give to certain values in our programs - variables are like containers for data.
    * Values can be of any data type; numbers, strings or even the results of operations.
    * Variables are important in programming because they let you perform operations on data that may change
* **Assignment** is the process of storing a value inside a variable.
    * A value is assigned to a variable by using the equal sign in the form of variable equals value
* An **expression** is a combination of numbers, symbols or other variables that produce a result when evaluated.

Below are some restrictions when naming variables in Python
1. Key words or functions that Python reserves for its own cannot be used as variable names
2. Variable names can't have any spaces and they must start with either a letter or an underscore
3. Variable names can only be made up of letters, numbers and underscores
4. Python variables are case sensitive

### Expressions, Numbers, and Type Conversion
* **Implicit conversion** takes plance when the interpreter automatically converts one data type into another.
* **Explicit conversion** takes place when a function is called to convert one data type into antother

---

## Functions
### Defining Functions
To define a function in Python,
1. Use the **def** keyword to define a function. The name of the function is what comes after the keyword. 
2. The parameters of the function are written between parentheses after the name.
3. The body of the function must be to the right of the definition.
Example:
    ```Python
    def greeting(name):
        print("Hello, " + name)
    ```

### Reutrning Values
The return statement allows us to:
* Combine calls to functions
* Perform more complex operations
* Makes the code more reusable
* **In Python, it can return more than one value**
 
* **Double slash operator (//)** is called **floor division**. A floor division divides a number and takes the integer part of the division as the result.
* **None** is a very special data type in Python used to indicate that things are empty or that they return nothing.

### Code Style
A few principles in mind to create good well styled code are:
1. Code to be self-documenting as possible
    * Self-documenting code is written in a way that's readable and doesn't conceal its intent. 
2. Leave a comment to add a bit of explanatory texts to the code
    * In Python, comments are indicated by the hash character

---

## Conditionals
### Compare Things
Equality operators allows us to take the result of the expressions and use them to make decisions
* a == b: a is equal to b
* a != b: a is different than b
* a < b: a is smaller than b
* a <= b: a is smaller or equal to b
* a > b: a is bigger than b
* a >= b: a is bigger or equal to b

Logical operators allow connecting multiple statements together and perform more complex comparisons
* a and b: True if both a and b are True. False otherwise.
* a or b: True if either a or b or both are True. False if both are False.
* not a: True if a is False, False if a is True.

**In Python uppercase letters are alphabetically sorted before lowercase letters**

### Branching with if Statements
**Branching** is the ability of a program to alter its execution sequence.

if block vs. defined function
| Similarities | Differences |
|:-|:-|
| * The keyword, either def or if, indicates the start of a special block
* Colon is used at the end of the first line
* The body of the function or the if block is indented to the right | * The body of the if block will only execute when the condition evaluates to true; otherwise, it skipped |

### else Statements
* The **modulo operator** is represented by the percentage sign (%) and __returns the remainder of the integer division between two numbers__. 
* **The integer division is an operation between integers that yields two results which are both integers, the quotient and the remainder.*
* When a return statement is executed, the function exits so that the code that follows doesn't get executed.

### elif Statements
The main difference between elif and if statements is that an elif block can be only written as as a companion to an if block.

---

## Credit
* [Coursera - Python Crash Course Week 2](https://www.coursera.org/learn/python-crash-course/home/week/2)