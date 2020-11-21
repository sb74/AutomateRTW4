#!/usr/bin/env python3
import os
import datetime
from reports import generate_report
from emails import generate_email, send_email

# Linux home directory.
home = os.path.expanduser("~")
# Text file directory.
txt_dir = home + r"/supplier-data/descriptions"

# Create title.
today_date = datetime.datetime.now()
title = (str(today_date).split(" ")[0])

# Create body text.
body = ""
for file in os.listdir(txt_dir):
    file_path = os.path.join(txt_dir, file)
    with open(file_path, "r") as description_file:
        # Read in and strip description into a list and append to new list.
        txt_content = description_file.readlines()
        txt_content = [line.strip() for line in txt_content]

        body += "name: " + txt_content[0] + "<br/>" + "weight: " + txt_content[1] + "<br/><br/>"

if __name__ == "__main__":
    # Generate pdf.
    generate_report("/tmp/processed.pdf", title, body)

    # Email details.
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"

    # Send pdf via email as attachment.
    message = generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    send_email(message)
