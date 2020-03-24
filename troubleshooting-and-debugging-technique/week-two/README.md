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

---

## When Slowness Problems Get Complex

---

## Credit

* [Coursera - Troubleshooting Debugging Techniques Week 2](https://www.coursera.org/learn/troubleshooting-debugging-techniques/home/week/2)
