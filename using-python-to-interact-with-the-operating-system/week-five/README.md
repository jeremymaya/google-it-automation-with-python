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

### Unit Tests
**Unit tests** are used to verify that __small isolated parts of a program are correct__.

An important characteristic of a unit test is **isolation**.

Unit test should only test the unit of code they target, the function or method that's being tested. This ensures that any success or failure of the test is caused by the behavior of the unit in question and doesn't result from some external factor like the network being down or a database server being unresponsive.

### Writing Unit Tests in Python

Use the **unittest module** which includes classes and methods for creating unit tests to write unit tests in Python.

### Edge Cases

Edge cases are inputs that produce unexpected results, and are found at the extreme ends of the ranges of input that programs could work with.

Some of the edge case examples for a function that expects a number include: 
* Passing zero to 
* Negative numbers
* Extremely large numbers

---

## Other Test Comcepts

### Black Box vs. White Box

* **White-box** testing, clear-box or transparent testing relies on the test creators knowledge of the software being tested to construct the test cases. 
    * White-box tests are helpful because a test writer can use their knowledge of the source code to create tests that cover most of the ways that the program behaves.


* **Black-box** tests or opaque testing are written with an awareness of what the program is supposed to do, its requirements or specifications, but not how it does it.
    * Black-box tests are useful because they don't rely on the knowledge of how the system works. This means their test cases are less likely to be biased by the code. They usually cover situations not anticipated by the programmer who originally wrote the script.

### Other Test Types

For different tests, separate **test environment** for test may be needed to runs a test version of our software that we're trying to verify.

* **Integration tests** take the individual modules of code that unit test verify then combine them into a group to test. It verify that the interactions between the different pieces of code in integrated environments are working as expected.
* **Regression test** is a variant of unit tests. It is usually written as part of a debugging and troubleshooting process to verify that an issue or error has been fixed once it's been identified. Regression tests are useful part of a test suite because they ensure that the same mistake doesn't happen twice.
* **Smoke test** sometimes called build verification test, get their name from a concept that comes from testing hardware equipment. 
    * Smoke test for a web service would be to check if there's a service running on the corresponding port
    * Smoke test for an automation script would be to run it manually with some basic input and check that the script finishes successfully
* **Load tests** verify that the system behaves well when it's under significant load.

Taking together a group of tests of one or many kinds is commonly referred to as a **test suite**.

### Test-Driven Development

**Test-driven development** or TDD is a process that calls for creating the test before writing the code.

**Continuous Integration** is a process that combines version control system and developmement processes. When engineers submit their code, it's integrated into the main repository and tests are automatically run against it to spot bugs and errors.

---

## Errors and Exceptions

### The Try-Except Construct
**Try-except construct** is useful when trying to handle possible errors that could happen instead of multiple if/else statements.

The code in the except block is only executed if one of the instructions in the try block raise an error of the matching type. To use a try-except block, be aware of the errors that functions that we're calling might raise.

### Raising Errors

---

## Credit

* [Coursera - Python Operating System Week 5](https://www.coursera.org/learn/python-operating-system/home/week/5)
