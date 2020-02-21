# Using Python to Interact with the Operating System - Week 6

## Interacting with the Command Line Shell

### Basic Linux Commands
A lot of commands come from Unix. The philosophy when designing how these programs should behave was that they should do one thing and do it very well. Which means there will be a lot of commands, each for doing specific thing.

Managing files and directories

* cd directory: changes the current working directory to the specified one
* pwd: prints the current working directory
* ls: lists the contents of the current directory
* ls directory: lists the contents of the received directory
* ls -l: lists the additional information for the contents of the directory
* ls -a: lists all files, including those hidden
* ls -la: applies both the -l and the -a flags
* mkdir directory: creates the directory with the received name
* rmdir directory: deletes the directory with the received name (if empty)
* cp old_name new_name: copies old_name into new_name
* mv old_name new_name: moves old_name into new_name
* touch file_name: creates an empty file or updates the modified time if it exists
* chmod modifiers files: changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable
* chown user files: changes the owner of the files to the given user
* chgrp group files: changes the group of the files to the given group

Operating with the content of files

* cat file: shows the content of the file through standard output
* wc file: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin
* file file: prints the type of the given file, as recognized by the operating system
* head file: shows the first 10 lines of the given file
* tail file: shows the last 10 lines of the given file
* less file: scrolls through the contents of the given file (press "q" to quit)
* sort file: sorts the lines of the file alphabetically
* cut -dseparator -ffields file: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

Additional commands

* echo "message": prints the message to standard output
* date: prints the current date
* who: prints the list of users currently logged into the computer
* man command: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)
* uptime: shows how long the computer has been running
* free: shows the amount of unused memory on the current system

### Redirecting Streams
* Redirection - the process of sending a stream to a different destination
    * Provided by OS
    * Use '>', greater symbol for redirect an output

```Bash
./stdout_example.py
./stdout_example.py > new_file.txt
```

After the second line, stoud.example.py is outputted in new_file.txt instead of inside of the terminal via STDOUT.

Be careful not to overwrite an existing file as redirection overwrites destination each time we perform a redirection of STDOUT.

* Append - sends a stream to a different destination and adds onto the existiing destination instead of overwriting it
    * Use '>>', double greater symbol to append

```Bash
./stdout_example.py
./stdout_example.py >> new_file.txt
```

These are the redirectors that we can use to take control of the streams of our programs

* command > file: redirects standard output, overwrites file
* command >> file: redirects standard output, appends to file
* command < file: redirects standard input from file
* command 2> file: redirects standard error to file

### Pipes
Pipe, |, connects multiple scripts, commands, or other programs together into a data processing pipeline. Pipes connect the output of one program to the input of another.
* command1 | command2: connects the output of command1 to the input of command2

Python scripts can be used with pipelines too. Python can read from standard input using the stdin file object provided by the sys module.

### Signalling Processes
Signals are tokens delivered to running processes to indicate a desired action.

These are some commands that are useful to know in Linux when interacting with processes.

* ps: lists the processes executing in the current terminal for the current user
* ps ax: lists all processes currently executing for all users
* ps e: shows the environment for the processes listed
* kill PID: sends the SIGINT signal to the process identified by PID
* fg: causes a job that was stopped or in the background to return to the foreground
* bg: causes a job that was stopped to go to the background
* jobs: lists the jobs currently running or stopped
* top: shows the processes currently using the most CPU time (press "q" to quit)

---

## Bash Scripting

### Creating Bash Scripts

**Bash** is the most commonly used shell on Linux. Bash is not only the interpreter that runs our commands, it's also a __scripting language__.

* ps command can list all the current running processes
* free command can show you the amount of free memory
* uptime command can tell you how long the computer has been on

### Using Variables and Globs

**Environment variables** are set in the environment in which the command is executing.

* = sign is used to set an environment variables
    * There can be no spaces between the name of the variable and the equal sign, or between the equal sign and the value
    * Any variable that you define in a script or in the command line is local to the environment where it was defined
* $ prefix is used to access the value of a variable
* export command to export commands from that environment

**Globs** are characters that allow us to create list of files. The star and question mark are the most common globs.
* using a \* in the command line will match all filenames that follow the format that we specify
* using a ? sign in the command line will match exactly one character instead of any amount of characters
    * ? can be repeated as many times as we need

### Conditional Execution in Bash

In bash scripting, the condition used is based on the exit status of commands, $?
* In bash scripting an exit value of zero means success.

**Test** is a command that evaluates the conditions received and exits with zero when they are true and with one when they're false.

---

## Advanced Bash Concepts

### While Loops in Bash Scripts
The loops in Bash starts with the **do** keyword and finishes with a **done** keyword.

To increment the value of the variable N, we're using a bash construct of double parentheses that lets us do arithmetic operations with our variables.

Below is an example while loop that runs up to 5 times:

```Bash
n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done
```

The value of a command line argument can be accessed by using the $1. In Python, we get the same information using sys.argv[1]

When rerunning scripts due to some kind of failure, sleep command may needed to wait a bit before trying again.

### For Loops in Bash Scripts
In Bash, we construct sequences of data by listing the elements with spaces in between. In Python, the sequences are data structures like a list or a tuple or a string.

```Bash
for fruit in peach orange apple; do
    echo "I like $fruit!"
done
```
To work with a list of file, we can use globs like star and question mark to create lists of files. These lists are separated by spaces and so we can use them in our loops to iterate over a list of files that match a criteria.

* Basename command takes a filename and an extension and then returns the name without the extension.
* Surround file variable with double-quotes to allow the command to work even if the file has spaces in its name.
    * This is a good practice in Bash scripts when dealing with file names or any variables that could include spaces.
* It is also good idea to first run the script without actually modifying the file system to catch any possible bugs that the script might have.
    * Add an echo in front of the MV command

### Choosing Between Bash and Python
Use Bash when we're operating with files and system commands, as long as what we're doing is simple enough that the script is self-explanatory.

Avoid using Bash as it becomes hard to understand what the script is doing. It's better to write it in a more general scripting language like Python.

Also Bash scripts aren't as flexible or robust as Python and some commands might not be present on certain operating system.

---

## Credit
* [Coursera - Python Operating System Week 6](https://www.coursera.org/learn/python-operating-system/home/week/6)