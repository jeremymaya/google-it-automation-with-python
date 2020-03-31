# Troubleshooting and Debugging Techniques - Week 3

## Why Programs Crash

### Systems That Crash

Reduce the scope of the problem by starting with the actions that are easier and faster to check.

1. Try looking at the logs to see if there's any error that may point to what's happening
2. Try moving away the local configuration for the program and using the default configuration/reinstall the application
3. Try checking if it is some hardware component failure

### What to do when you can't fix the program

Use **Wrappers** when the expected output and input formats don't match. A **Wrapper** is a function or program that provides a compatibility layer between two functions or programs so they can work well together.

Run the application inside a **virtual machine** or maybe a **container** if there's another application that requires a different version of the same library or you can't change a certain configuration setting because it's required to access a different service.

Deploy a **watchdog** when we can't find a way to stop an application from crashing but we can make sure that if it crashes it starts back again. This is a process that checks whether a program is running and when it's not starts the program again. To implement this, write a script that stays running in the background and periodically checks if the other program is running.

Share good reproduction case and answer the questions wgeb reporting a bug by answering following questions.

* What were you trying to do?
* What were the steps you followed?
* What did you expect to happen?
* What was the actual outcome?

### Internal Server Error

When a webpage on a Web server isn't working,

1. Try looking at logs
    * On Linux systems, logs are located in Bar log
    * Use the date command to check the current date
2. Use the netstat command which can give us information about our network connections depending on the flags  passed
    * This command accesses different sockets that are restricted to route the administrator user on Linux - call it with sudo
    * Run commands as root, and then pass different flags with netstat
    * Use -n to print numerical addresses instead of resolving host names
    * Use L to only check out the sockets that are listening for connection
    * Use P to print the process ID and name to which each socket belongs
    * Since we are interested in port 80, connect the output to a grep command checking for colon 80 - the Web server is usually running on port 80, the default web serving port

## Code that Crashes

## Handling Bigger Incidents

---

## Credit

* [Coursera - Troubleshooting Debugging Techniques Week 3](https://www.coursera.org/learn/troubleshooting-debugging-techniques/home/week/3)
