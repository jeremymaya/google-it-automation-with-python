# Troubleshooting and Debugging Techniques - Week 2

## Understanding Slowness

The general strategy for addressing slowness is to **identify the bottleneck** for addressing slowness in  device, script, or system to run slowly.

Monitor the usage of resources to know which of them as being exhausted.

Top tool on Linux systems lets us see which currently running processes are using the most CPU time.

* There are other tools we can use like iotop and iftop

### Possible Causes for Slowness

When you can't modify the code of the program, try to **reduce** the size of the files involved

* If the file is a log file, you can use a program like logrotate to do this for you.

### Slow Web Server

Use a tool called **ab** which stands for **Apache Benchmark** tool to figure out how slow the server is

* Run ab -n 500 to get the average timing of 500 requests, and then pass a web address for the measurement

---

## Slow Code

### Writing Efficient Code

As a rule, aim first to write code that is to avoid bugs

* Readable
* Easy to maintain
* Easy to understand

If the code is not fast enough, tru to optimize by eliminating **expensive actions**, which are those that take a long time to complete.

* Trying to optimize every second out of a script is probably not worth the effort though

The first step is to keep in mind that we can't really make our computer go faster. If we want our code to finish faster, we need to make our computer do less work, and to do this, we'll have to 

1. Avoid doing work that isn't really needed
2. Avoid calculating data repeatedly by using the right data structures and storing the data
3. Reorganize the code so that the computer can stay busy while waiting for information from slow sources like disk or over the network

Use a **profiler** tool to measure the resources that the code is using for better understanding of what's going on. It allows us to see which functions are called by our program, how many times each function was called and how much time are programs spent on each of them.

Because of how profilers work, they are specific to each programming language

* C program uses gprof to analyze
* Python uses c-Profile module to analyze

---

## When Slowness Problems Get Complex

---

## Credit

* [Coursera - Troubleshooting Debugging Techniques Week 2](https://www.coursera.org/learn/troubleshooting-debugging-techniques/home/week/2)
