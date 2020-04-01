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

### Accessing Invalid Memory

One common reason a program crashes is it's trying to access invalid memory. Accessing invalid memory means that the process tried to access a portion of the system's memory that wasn't assigned to it.

In low-level languages like C or C++, the variables that store memory addresses are called pointers and the programmer needs to take care of requesting the memory that the program is going to use and then giving that memory back once it's not needed anymore.

When a program tries to read or write to a memory address outside of the valid range, OS will raise an error like **segmentation fault** or **general protection fault**.

Common programming errors that lead to segmentation faults or segfaults include,

* Forgetting to initialize a variable
* Trying to access a list element outside of the valid range
* Trying to use a portion of memory after having given it back
* Trying to write more data than the requested portion of memory can hold

The **debugger** can give you a lot more detail on what the application is doing and why the memories invalid. For this to be possible, we'll need our program to be compiled with debugging symbols. This means that on top of the information that the computer uses to execute the program, the executable binary needs to include extra information needed for debugging, like the names of the variables and functions being used.

Linux distributions like Debian or Ubuntu ships separate packages with the debugging symbols for all the packages in the distribution. Microsoft compilers can also generate debugging symbols in a separate PDB file.

**Valgrind** can help when trying to understand problems related to handling invalid memory. Valgrind is a very powerful tool that can tell us if the code is doing any invalid operations no matter if it crashes are not. Valgrind lets us know if the code is accessing variables before initializing them.

Valgrind is available on Linux and Mac OS, and Dr. Memory is a similar tool that can be used on both Windows and Linux.

### Unhandled Errors and Exceptions

When a program comes across an unexpected condition that isn't correctly handled in the code, it will trigger errors or exceptions.

In Python, following errors could occurs,

* Index error if we tried to access an element after the end of a list
* Type error or an attribute error if we try to take an action on a variable that wasn't properly initialized
* Division by zero error if we tried to divide by zero

When these failures happen, the interpreter that's running the program will print the following:

* Type of error
* Line that caused the failure
* **Traceback** which shows the lines of the different functions that were being executed when the problem happened

To find out where things are going wrong, we use **debugging tools** available for the application's language

For a Python, program we can use the **BDB interactive debugger** which lets us do all the typical debugging actions like executing lines of code one-by-one or looking at how the variables change values.

When we're trying to understand what's up with a misbehaving function on top of using debuggers, it's 

**print f debugging** is a common practice to trying to understand what's up with a misbehaving function on top of using debuggers. It adds statements that print data related to the codes execution to show the contents of variables, the return values of functions or metadata like the length of a list or size of a file. Taking a step further, the best approach is to add the messages in a way that can be easily enabled or disabled depending on whether we want the debug info or not.

In Python, use the **logging module** which lets us set how comprehensive we want our code to be.

### Fixing Someone Else's Code

Writing good comments is one of those good habits that pays off when trying to understand code written by others and also your past self.

Another thing that can help to understand someone else's code is reading the tests associated to the code.

### Debugging a Segmentation Fault

When an application crashes, it's useful to have a **core file** of the crash.

**Core files** store all the information related to the crash so that we or someone else can debug what's going on. It's like taking a snapshot of the crash when it happens to analyze it later.

In order to enable OS to generate core file,

1. Run the ulimit command
2. Use the -c flat for core files
3. use the unlimited to state that we want core files of any size

For the exercise show in the video, it debugs **off-by-one error** by

1. Generated a core file and check the file using LS-L command
2. Use gdb-c core to give it a core file and then example to tell it where the executable that crashed is located
3. Use the backtrace command to look at the full backtrace of the crash
4. Use the list command that shows the lines around the current one to get more contexts for the code that failed
5. Print the contents of the first element argv 0, and then the second element argv 1
    * Zero is never a valid pointer

## Handling Bigger Incidents

### Crashes in Complex Systems

Below is troubleshoot strategies that can be used when handling crashes in complex systems,

1. Roll back
    * It is the best strategy to use when the new changes are supsected to be causing the issue
    * It restores the service back to health if it was the cause
    * It helps eliminate new change as a possible cause if doing the rollback doesn't help
2. Logs with useful information
3. Monitoring of what the service is doing and version control for qucik roll back if needed
4. Deploy new machines if needed

### Communication and Documentation During Incidents

Forgetting to dcoument could:

* Risk forgetting some important details
* Wasting a lot of valuable time when the same issue is revisited

Good document should contain the following:

* Root cause
* How you diagnose the problem and found that root cause
* What you did to fix the issue and what needs to be done to prevent the problem from happening again

### Writing Effective Postmortems

**Postmortems** are documents that describe details of incidence to help us learn from our mistakes. The goal of postmortems is to learn from what happened to prevent the same issue from happening again.

In general postmortem should inclde include:

* Details of what caused the issue
* What the impact of the issue was
* How it got diagnosed
* Short-term remediation you applied
* Long-term remediation you recommend

---

## Credit

* [Coursera - Troubleshooting Debugging Techniques Week 3](https://www.coursera.org/learn/troubleshooting-debugging-techniques/home/week/3)
