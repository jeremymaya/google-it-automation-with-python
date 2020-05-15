# Automating Real-World Tasks with Python - Week 2

## Learning Objectives

Look into different tools that can be really useful in today's IT world by:

* Learning how you can use different text formats to store data in text files, retrieve it, and even transmit it over the internet
* Learning how we can get our code to interact with services running on different computers using a module called Python Requests

---

## Web Applications and Services

### Web Applications and Services (sub)

A **web application** is an application that you interact with over HTTP. Most of the time when you’re using a website on the Internet, you’re interacting with a web application.

A **web service** is a web applications that have an API.

* Instead of browsing to a web page to type and click around, you can use your program to send a message known as an **API call** to the web service's API endpoints.

### Data Serialization

**Data serialization** is the process of taking an in-memory data structure, like a Python object, and turning it into something that can be stored on disk or transmitted across a network. (ex: CSV file)

Turning the serialized object back into an in-memory object is called **deserialization**.

A web service's API endpoint can take messages in a specific format, containing specific data such as serialized data.

### Data Serialization Formats

There are different data serialization formats:

* JavaScript Object Notation (JSON)
* Yet Another Markup Language (YAML)
* Python pickle
* Protocol Buffers
* eXtensible Markup Language (XML)

JSON (JavaScript Object Notation) is the serialization format that is used widely today in IT.

Below code uses the ```json.dump()``` function to serialize the people object into a JSON file.

```Python
import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
```

Below is output of the ```json.dump()```

```JSON
[
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  },
]
```

### More About JSON

Characateristics of JSON incliudes:

* JSON is human-readable
* JSON elements are always comma-delimited

JSON supports a few elements of different data types such as:

* Strings
* Numbers
* Objects
* Key-Value pair
* Arrays - arrays can contain strings, numbers, objects, or other arrays

```JSON
[
  "apple",
  "banana",
  12345,
  67890,
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  }
]
```

---

## Python Requests

### The Python Requests Library

HTTP (HyperText Transfer Protocol) is the protocol of the world-wide web

---

## Credit

* [Coursera - Automating Real World Tasks Python Week 2](https://www.coursera.org/learn/automating-real-world-tasks-python/home/week/2)
