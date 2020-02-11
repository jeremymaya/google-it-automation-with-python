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

### Command-Line Arguments and Exit Status

**Command line arguments** are parameters that are passed to a program when it started.

* Allows a code of the script to be generic
* Allows scripts to run automatically without requiring any interactive user input
* Useful for system administration tasks as it allow us to specify the information that we want our program to use

Parameter values can be accessed using the **argv** in the **sys** module.

**Exit status** or **return code** is a value returned by a program to the shell. It provides another source of information between the shell and the programs that get executed inside of it.

To see what the exit status of the last executed command was use the following commands:

* Use ?$ to see the contents
* Use wc to count the number of lines words and characters in a file


### Obtaining the Output of a System Command

The **host** command converts a host name to an IP address and vice versa.

The **decode function** applies an encoding to transform the bytes into a string
* It uses a UTF-8 encoding by default

### Advanced Subprocess Management

The usual strategy for modifying the environment of a child process is:

1. Copy the environment seen by the process
2. Do any necessary changes
3. Pass the changed environment as the environment that the child process will see

The **copy method** of the OS environ creates a new dictionary that can be changed as needed without modifying the original environment
The **path variable** indicates where the operating system will look for the executable programs

Some of parameters that can be used with the run function includes:

* The CWD parameter which changes the current working directory where the command will be executed.
    * Useful when working with a set of directories where you need to run a command on each of them.
* The timeout parameter which cause the run function to kill the process if it takes longer than a given number of seconds to finish.
    * Useful if you're running a command that you know might get stuck.
* The shell parameter which if set to true, Python will first execute an instance of the default system shell and then run the given command inside of it.
    * Useful if command line needs include variable expansions and other shell operations.

---

## Processing Log Files

### Filtering Log Files with Regular Expressions
The usual technique to operate on files is to:

1. Call the open function which returns a file object
2. Iterate through each of its lines using a for-loop

For performance reasons, when files are large, it's generally a good practice to read them line by line instead of loading the entire contents into memory.

## Credit

* [Coursera - Python Operating System Week 4](https://www.coursera.org/learn/python-operating-system/home/week/4)
