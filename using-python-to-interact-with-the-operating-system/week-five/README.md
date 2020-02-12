# Using Python to Interact with the Operating System - Week 5

## Simple Tests

### What is testing?

Software testing is a process of evaluating computer code to determine whether or not it does what you expect it to do.

Writing tests can help wth:

* Eliminate bugs
* Improve the reliability and the quality of automation

### Manual Testing and Automated Testing

The **manual testing** is the most basic way of testing a script by running the test with different parameters and see if it returns the expected values.

The automatic testing is codifying tests into its own software and code that can be run to verify that the programs do what we expect them to do. The goal of automatic testing is to automate the process of checking __if the returned value matches the expectations__.

---

## Unit Tests

**Unit tests** are used to verify that __small isolated parts of a program are correct__.

An important characteristic of a unit test is **isolation**.

Unit test should only test the unit of code they target, the function or method that's being tested. This ensures that any success or failure of the test is caused by the behavior of the unit in question and doesn't result from some external factor like the network being down or a database server being unresponsive.

---

## Credit

* [Coursera - Python Operating System Week 5](https://www.coursera.org/learn/python-operating-system/home/week/5)
