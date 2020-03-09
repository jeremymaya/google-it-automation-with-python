# Troubleshooting and Debugging Techniques - Week 1

## Introduction to Debugging

### What is debugging

Problems may caused by the any of the following:

* Hardware
* The operating system
* Applications running on the computer
* The environment and configuration of the software

**Troubleshooting** is the process of identifying, analyzing, and solving problems while **Debugging** is the process of identifying, analyzing, and removing bugs in a system.

But generally, we say troubleshooting when we're fixing problems in the system running the application, and debugging when we're fixing the bugs in the actual code of the application.

**Debuggers** let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more.

There are different tools for debugging:

* tcpdump and Wireshark: shows ongoing network connections, and help with analyzing the traffic going over the cables
* ps, top, or free: shows the number and types of resources used in the system
* strace: shows the system calls made by a program
* ltrace: shows the library calls made by the software

### Problem Solving Steps

1. Gathering as much information from any of the existing documentation
    * The current state of things
    * What the issue is
    * When it happens
    * What the consequences are
    * Reproduction case, which is a clear description of how and when the problem appears
2. Find the root cause of the problem
3. Perform the necessary remediation
    * Workaround can be used when we could understand the problem just enough and try our users get back to work quickly
    * Ultimately, prevent the problem from occurring to save time in the future

Also document the debugging process for the future referece.

---

## Understanding the Problem

---

## Binary Searching a Problem

---

## Credit

* [Coursera - Troubleshooting Debugging Techniques Week 1](https://www.coursera.org/learn/troubleshooting-debugging-techniques/home/week/1)
