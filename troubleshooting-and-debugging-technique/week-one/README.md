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

### It Doesn't Work

There are some common questions that we can ask a user that simply report something doesn't work:

* What were you trying to do?
* What steps did you follow?
* What was the expected result?
* What was the actual result?

When debugging a problem, we want to consider the simplest explanations first and avoid jumping into complex or time-consuming solutions unless we really have to.

After having a basic idea of what the problem is, figure out the root cause by applying a process of elimination, starting with the simplest explanations first and testing those until you can isolate the root cause.

### Creating a Reproduction Case

A **reproduction case** is a way to verify if the problem is present or not. When trying to create a reproduction case, we want to find the actions that reproduce the issue, and we want these to be as simple as possible. The smaller the change in the environment and the shorter the list of steps to follow, the better.

When debugging, the first step is to **read the logs**. Which logs to read, will depend on the operating system and the application that you're trying to debug.

* On Linux, read system logs like /var/log/syslog and user-specific logs like the.xsession-errors file located in the user's home directory
* On MacOs, on top of the system logs, go through the logs stored in the library logs directory
* On Windows, use the Event Viewer tool to go through the event logs

### Finding the Root Cause

Understanding the root cause is essential for performing the long-term remediation.

Whenever possible, we should check our hypothesis in a __test environment__, instead of the production environment that our users are working with.

### Dealing with Intermitent Issues

When dealing with intermitent issues,

1. Get more involved in what's going on, so that you understand when the issue happens and when it doesn't
    * Usually invovles going through logs or enabling debugging information
2. Look at different sources of information, like the load on the computer, the processes running at the same time, the usage of the network, and so on

If a problem goes away by turning it off and on again, there's almost certainly a bug in the software, and the bug probably has to do with not managing resources correctly.

---

## Binary Searching a Problem

### What is binary search

**Linear search** works but the longer the list, the longer it can take to search.

If the list is **sorted**, we can use an alternative algorithm for searching called **binary search**.

* It may take more time to sort an unsorted list to perform binary search
* It can still make sense to do it if we're going to search through it several times
* It doesn't make sense to sort the list and then use binary search to only find one element. In that case, using linear search is simpler and faster.

### Applying Binary Search in Troubleshooting

In troubleshooting, we can apply **bisecting** to go through and test a long list of hypotheses. When doing this, the list of elements contains all the possible causes of the problem and we keep reducing the problem by half until only one option is left.

When using Git for version control, we can use a __Git command called **bisect**__. Bisect receives two points in time in the Git history and repeatedly lets us try the code at the middle point between them until we find the commit that caused the breakage.

### Finding Invalid Data

wc command - counts characters, words, and lines in a file
head command - prints the first lines in the file, and the tail command to print the last lines

---

## Credit

* [Coursera - Troubleshooting Debugging Techniques Week 1](https://www.coursera.org/learn/troubleshooting-debugging-techniques/home/week/1)
