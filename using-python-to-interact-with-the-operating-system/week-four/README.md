# Using Python to Interact with the Operating System - Week 4

## Data Streams
### Reading Data Interactively
Use **input function** to prpmpt the user for a certain value which can be used in a script.

### Standard Streams
**I/O streams** are the basic mechanism for performing input and output operations in your programs.

Most operating systems supply three different I/O streams by default each with a different purpose which aren't restricted to just Python.
* STDIN - the standard input stream which is a channel between a program and a source of input
* STDOUT - the standard output stream which is a pathway between a program and a target of output
* SDTERR - the standard error stream which displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program

### Environment Variables
A **shell** is a command line interface used to interact with your operating system. Python programs get executed inside a shell command-line environment. 

The **variable set** in that environment are another source of information that can be used in scripts.

**Echo** is a command that prints texts in Linux shell. In order to access the value of the variable in the shell, use a prefix and name of the variable with a dollar sign.
```Bash
echo $PATH
```
In order to access environment variables, use the **Environ dictionary** provided by the OS module.

---

## Credit
* [Coursera - Python Operating System Week 3](https://www.coursera.org/learn/python-operating-system/home/week/3)