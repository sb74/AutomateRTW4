#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, receiver, subject, body, attachment=None):
    message = email.message.EmailMessage()

    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)

    # Add attachment.
    if attachment is not None:
        attachment_name = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split("/", 1)
        with open(attachment, 'rb') as fp:
            message.add_attachment(fp.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_name)

    return message


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

    return
