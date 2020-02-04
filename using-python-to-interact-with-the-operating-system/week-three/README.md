# Using Python to Interact with the Operating System - Week 3

## Regular Expressions
### What is regualr expressions?
A regular expression, also known as regex or regexp, is essentially a search query for text that's expressed by __string pattern__. It allows for searching a text for strings matching a specific pattern.

When a particular piece of text searched using regex, anything that matches a regular expression pattern you specified, is returned as a result of the search. 

### Why use regular expressions?
Regex allows for flexibility in string searching and avoids using brittle solution such as index function.

### Basic Matching with grep
Grep grep works by printing out any line that matches the passed query.

grep __case sensitive__ example to search for "thon":
```bash
grep thon /usr/share/dict/words
```

grep __case insensitive__ example to search for "thon":
```bash
grep -i thon /usr/share/dict/words
```

Reserved characters to process an irregular expressions in regex:
* ".", dot, matches any character which means that it can be used as a wildcard that can be replaced by any other character in the results.
* "^", caret or circumflex, indicates the beginning of the line. 
* "$", dollar, indicates the end of the line.

grep . example to search for a string mathching with "l.rts":
```bash
grep l.rts /usr/share/dict/words
```

grep cafrat example to search for a string starting with "fruit":
```bash
grep ^fruit /usr/share/dict/words
```

grep $ example to search for a string ending wiht "cat":
```bash
grep cat$ /usr/share/dict/words
```

---

## Basic Regular Expressions

---

## Advanced Regular Expressions

---

## Credit
* [Coursera - Python Operating System Week 3](https://www.coursera.org/learn/python-operating-system/home/week/3)