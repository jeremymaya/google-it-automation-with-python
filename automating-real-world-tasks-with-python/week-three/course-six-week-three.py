from email.message import EmailMessage
import os, smtplib, ssl, getpass, mimetypes

def generate_email_with():
    # creates an empty email message
    message = EmailMessage()

    sender = "jeremiah.kim.spam@gmail.com"
    recipient = "jeremiah.kim.spam@gmail.com"

    # adds the sender, recipient, and subject to the message
    # From, To, and Subject form email header fields
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

    # adds message by using set_content method
    body = """Hey there!

    I'm learning to send emails using Python!"""
    message.set_content(body)

    add_attachment(message)

    return sender, message

def add_attachment(message):
    attachment_path = os.curdir + ("/tmp/example.png")

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

def send_email_through_smtp(sender, message):
    # https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server
    # https://support.google.com/mail/answer/7126229?hl=e

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        # server.set_debuglevel(1)
        mail_pass = getpass.getpass('Password? ')
        server.login(sender, mail_pass)
        server.send_message(message)

sender, message = generate_email_with()
send_email_through_smtp(sender, message)
