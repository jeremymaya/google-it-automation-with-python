# Crash Course of Python - Week 4

## Learning Objectives
* Understand the difference between strings, lists, and dictionaries
* Manipulate strings in your code
* Create and use lists
* Create and use dictionaries

---

## String
### What is a string?
A **string** is a data type in Python that's used to represent a piece of text.

Strings can be concatenated to build longer strings by using the plus sign or multiplied by a number, which multiplies the content of the string that many times.

### The Parts of a String
The **string indexing** operation accesses the character in a given position or index using square brackets and the number of the position specified
* string[0]
* To access the last character of a string, use negative indexes
* A **slice** is the portion of a string that can contain more than one character (ex. string[1:4])

### Creating New Strings
Strings in Python are immutable, meaning __they can't be modified__.

### Formatting Strings
String operations
* len(string) Returns the length of the string
* for character in string Iterates over each character in the string
* if substring in string Checks whether the substring is part of the string
* string[i] Accesses the character at index i of the string, starting at zero
* string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

String methods
* string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
* string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
* string.count(substring) Returns the number of times substring is present in the string
* string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
* string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
* string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
* string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
* delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter

---

## Lists
### What is a list?
Square brackets are used to indicate where the list starts and ends in Python.

In Python, strings and lists are both examples of **sequences**. There are other sequences too, and they all share operations like:
* Iterating over them using for-loops
* Indexing using the len function to know the length of the sequence
* Using plus to concatenate two sequences
* Using in to verify if the sequence contains an element

### Modifying the Contents of a List
One of the ways that lists and strings are different is that lists are mutable. Which is another fancy word to say that they can change. This means we can add, remove, or modify elements in a list.
* The append method adds a new element at the end of the list. 
* The insert method inserts an element in a different position, instead of at the end, by taking an index as the first parameter and an element as the second parameter.
* The remove method removes an element 
* The pop method can also remove an element and receives an index

### Lists and Tuples
* **Strings** are sequences of characters and are **immutable**.
* **Lists** are sequences of elements of any type and are **mutable**.
* **Tuples** are sequences of elements of any type that are **immutable**.
    * When using tuples the position of the elements inside the tuple have meaning.
    * Tuples can be **unpacked** whichwe can turn a tuple of elements into separate variables. 

Examples of tuples include:
* When a function returns more than one value, it's returning a tuple.
* Store a filename and it's size
* Store the name and email address of a person
* Store a date and time and the general health of the system at any point in time

### Iterating over Lists and Tuples
Use **enumerate** method when iterate over lists or tuples.

Using range method works BUT it's more idiomatic in Python to iterate through the elements of the list directly or using enumerate when we need the indexes.

### List Comprehension
Since creating lists based on sequences is such a common task, Python provides a technique called **list comprehension**, which allows it to be done in just one line. __List comprehensions let us create new lists based on sequences or ranges.__

---

## Dictionaries
### What is a dictionary?
**Dictionaries** take the form of pairs of keys and values to store data.
* Dictionaries are mutable
* Unlike lists, elements cannot be accessed using their position

#### Definition
x = {key1:value1, key2:value2}

#### Operations
* len(dictionary) - Returns the number of items in the dictionary
* for key in dictionary - Iterates over each key in the dictionary
* for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
* if key in dictionary - Checks whether the key is in the dictionary
* dictionary[key] - Accesses the item with key key of the dictionary
* dictionary[key] = value - Sets the value associated with key
* del dictionary[key] - Removes the item with key key from the dictionary

#### Methods
* dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
* dict.keys() - Returns a sequence containing the keys in the dictionary
* dict.values() - Returns a sequence containing the values in the dictionary
* dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
* dict.clear() - Removes all the items of the dictionary
---

## Credit
* [Coursera - Python Crash Course Week 4](https://www.coursera.org/learn/python-crash-course/home/week/4)
* [Python Documentation - Common string operations](https://docs.python.org/3/library/string.html)
* [Python Documentation - String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
* [Python Documentation - Dictionary](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)