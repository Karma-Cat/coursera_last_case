#!/usr/bin/env python3

import os
import datetime
import reports
import emails

attachment = "/tmp/processed.pdf"

_data = datetime.date.today()
data = _data.strftime("%B %d, %Y")

title = "Processed Update on {}".format(data)

path = "/supplier-data/descriptions/"
dataKeys = ['name', 'weight']

files = os.listdir("path")
paragraph = []
for file in files:
    with open(path+file, 'r') as file_r:
	    name = file_r.readlines()[0]
        weight = file_r.readlines()[1]
        paragraph.append("name:{}\nweight:{}".format(name, weight))

if __name__ == "__main__":
    reports.generate_reports(attachment, title, paragraph)
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send(message)
