# Automating Real-World Tasks with Python - Week 3

## Learning Objectives

Look into a different aspect of automation: automating the generation of nicely formatted output from  scripts, like sending emails by:

* Learning how to create the contents of the email or the PDF
* Learning how to attach a file to an email
* Learning how to send the email to an SMTP server

---

## Sending Emails from Python

### Introduction to Python Email Library

Instead of constructing emails message based on the **Simple Mail Transfer Protocol (SMTP)** and **Multipurpose Internet Mail Extensions (MIME)** standards, we can use Python's EmailMessage module to easily construct email messages.

Email object created using EmailMessage module consists of **email header fields** and **message body**.

**Email header fields** are **key-value pair** labels that instructs email clients and servers to route and display the email. Email header fields include:

* From
* To
* Subject

Email object's message body is set using the the ```set_content()``` methods. The ```set_content()``` method adds the following additional headers for encoding:

* Content-Type
* Content-Transfer-Encoding

```Python
from email.message import EmailMessage

# creates an empty email message
message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

# adds the sender, recipient, and subject to the message
# From, To, and Subject form email header fields
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

# adds message by using set_content method
body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)
```

### Adding Attachments

The attachment for email needs to be labeled with a MIME type and subtype in order for the recipient to understand what to do with an attachment. We can use Python's mimetypes module to determine attachment type and subtype.

```Python
import os.path, mimetypes
attachment_path = "/tmp/example.png"

# uses the Python mimetypes module to determine attachment type and subtype 
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

# splits mime_type string into the MIME type and subtype
mime_type, mime_subtype = mime_type.split('/', 1)

# opens and adds the attachment the message
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
```

### Sending the Email Through an SMTP Server

Computers use the Simple Mail Transfer Protocol (SMTP) to send emails which is a protocol that specifies how computers can deliver email to each other. We can use Python's smtplib module to send email messages.

For more information, read [Sending Emails With Python](https://realpython.com/python-send-email/).

```Python
import smtplib

# creates an object that will represent a mail server which handles sending messages to the server
mail_server = smtplib.SMTP('localhost')

# establishes a secrue connection to the remote server using SSL/TLS protocol
mail_server = smtplib.SMTP_SSL('smtp.example.com')

# sets the debug level on the SMTP object
mail_server.set_debuglevel(1)

import getpass

# uses the getpass module to get password - mail_pass variable is still a string
mail_pass = getpass.getpass('Password? ')

# authenticates to the email server using the SMTP object's login method
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()
```

---

## Generating PDFs from Python

---

## Credit

* [Coursera - Automating Real World Tasks Python Week 3](https://www.coursera.org/learn/automating-real-world-tasks-python/home/week/3)
