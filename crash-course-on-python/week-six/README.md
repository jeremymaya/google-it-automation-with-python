# Crash Course of Python - Week 6

## Writing a Script from the Group Up
### Problem Statement
Create a daily report that tracks the use of machines. Specifically, create report that generates  which users are currently connected to which machines.

### Criteria
#### Input
An instance of the event class which will contains the following:
* The date when the event happened
* The name of the machine where it happened
* The user involved
* The event type, which includes the login and logout event type
    * The event types are strings and the ones we care about are login and logout

The class event has the following attributes:
* date
* user
* machine
* type 
#### Output
Print the machine name followed by all the current users separated by commas.

### Apprach
1. Sort the list of events chronologically.
2. Store the data in a dictionary of sets
    * We need keep track of who's logged into which machine
    * Set provides O(n) search 
3. Print the dictionary

## Final Project
### Problem Statement
Create a "word cloud" from a text by procssing the text and return a dictionary that outputs the frequency of each words.

### Criteria
#### Input
* Processing the text
* Remove punctuation
* Ignore case and words that do not contain all alphabets
* Count the frequencies
* Ignore uninteresting or irrelevant words

#### Output
A dictionary is the output of the calculate_frequencies function. The wordcloud module will then generate the image from your dictionary.

### Apprach
1. Browse and upload a text to be processed
2. Remove puntuations and normalize the letters
3. Create a set to store the uninteresting words
4. Create a dictionary that uses a word as a key and frequencies of the word as a value
5. Use WordCloud framework to generate a image of world cloud 

### Visual (The Sun Also Rises by Ernest Hemingway)
![course-one-final-project](https://github.com/jeremymaya/google-it-automation-with-python/blob/master/assets/course-one-final-project.png)

---

## Credit
* [Coursera - Python Crash Course Week 6](https://www.coursera.org/learn/python-crash-course/home/week/6)
* [Guthenberg Project - The Sun Also Rises by Ernest Hemingway](https://gutenberg.ca/ebooks/hemingwaye-sunalsorises/hemingwaye-sunalsorises-00-h.html)
