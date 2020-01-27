# Crash Course of Python - Week 6

## Writing a Script from the Group Up
### Problem Statement
Create a daily report that tracks the use of machines. Specifically, create report that generates  which users are currently connected to which machines.

### Criteria
#### Input
An instance of the event class which will contains the following:
* The date when the event happened
* The name of the machine where it happened
* The user involved
* The event type, which includes the login and logout event type
    * The event types are strings and the ones we care about are login and logout

The class event has the following attributes:
* date
* user
* machine
* type 
#### Output
Print the machine name followed by all the current users separated by commas.

### Apprach
1. Sort the list of events chronologically.
2. Store the data in a dictionary of sets
    * We need keep track of who's logged into which machine
    * Set provides O(n) search 
3. Print the dictionary

---

## Credit
* [Coursera - Python Crash Course Week 6](https://www.coursera.org/learn/python-crash-course/home/week/6)