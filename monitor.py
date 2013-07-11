#!/usr/bin/python

import smtplib
import os
import time
import datetime
from myconfig import *

server = 'smtp.gmail.com'
port = 587
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

"Sends an e-mail to the specified recipient."
sender = monitor_email
recipient = recipient_email
subject = 'Server Monitor Alert'
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
session = smtplib.SMTP(server, port)
session.ehlo()
session.starttls()
session.ehlo
session.login(monitor_email, monitor_pwd)
response = os.system("ping -c 1 " + hostname)

if response == 0: #if down, send an email
	body = hostname + " " + "is down at" + " " + st	
	session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
	session.quit()
else: #do nothing
	session.quit()
  

