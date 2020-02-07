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
### Simple Matching in Python
* The "r" at the beginning of the pattern indicates that this is a rawstring.
    * Always use rawstrings for regular expressions in Python.
* __None__ is a special value that Python uses that show that there's none actual value there.
* The **match attribute** always has a value of the actual sub string that match the search pattern.
* The **span attribute** indicates the range where the sub string can be found in the string.
* Additional options to the search function can be added as a third parameter.
    * The re.IGNORECASE option returns a match that is case insensitive

### Wildcards and Character Classes
A **wildcard** can match more than one character.
* . in a regular expressions as a special character that can match any character.
* Using a . is the broadest possible wildcard because it matches absolutely any character.

Character classes are written inside square brackets, []:
* It list the characters to match inside of the brackets
* A range of characters can be defined using a dash
* Use a ^, circumflex, inside the square brackets to match any characters that aren't in a group.
* Use a |, pipe symbol to match either one expression or another

The **search function** returns the __first matching string only__ when there are multiple matches. Use the **findall function** provided by the re module to get __all possible matches__.

### Repetition Qualifiers
Repeated matches can be searched using the expressions below:
* Use a . followed by * to matches any character repeated as many times as possible including zero - greedy behavior.
* Use a +, plus character, to match one or more occurrences of the character that comes before it.
* Use a ?, question mark symbol, for either zero or one occurrence of the character before it.
    * It is used to specified optional characters

### Escaping Characters
A pattern that includes a \ could be escaping a special regex character or a special string character
* Use a \, escape character, to match one of the special characters
* Use a \w to match any alphanumeric character including letters, numbers, and underscores
* Use a \d to match digits
* Use a \s for matching whitespace characters like space, tab or new line
* Use a \b for word boundaries

---

## Advanced Regular Expressions
### Capturing Groups
Use parentheses to capture groups which are portions of the pattern that are enclosed in
* The group method returns a tuple of two elements
* Use indexing to access these groups
* The first element contains the text matched by the entire regular expression
* Each successive element contains the data that was matched by every subsequent match group

### More on Repetition Qualifiers
* Use {}, curly brackets and one or two numbers to specify a range with numeric repetition qualifiers.
* Use \b, which matches word limits at the beginning and end of the pattern, to match full words.

### Splitting and Replacing
Split function from the re module works by taking any regular expression as a separator
* Use capturing parentheses to split list to include the elements that is used to split the values

Sub function from the re module is used for creating new strings by substituting all or part of them for a different string
* It uses regular expressions for both the matching and the replacing

---

## Credit
* [Coursera - Python Operating System Week 3](https://www.coursera.org/learn/python-operating-system/home/week/3)