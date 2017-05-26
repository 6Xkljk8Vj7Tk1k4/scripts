#!/usr/bin/env python

#
# usage:
# ./sendemail.py "subject" "email body"
#

import smtplib, sys
from email.mime.text import MIMEText

sender = 'sender@domain.ltd'
recipients = ['user1@domain.ltd', 'user2@domain.ltd']

msg = MIMEText(sys.argv[2])
msg['Subject'] = sys.argv[1]
msg['From'] = sender
msg['To'] = ", ".join(recipients)

s = smtplib.SMTP('mail.domain.ltd', 25)
s.login("sender@domain.ltd","password")
s.sendmail(sender, recipients, msg.as_string())
s.quit()
