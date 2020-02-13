#!/usr/bin/env python

#
# usage:
# ./sendemail.py "subject" "email body"
#

import sys
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP

sender = 'sender@domain.ltd'
recipients = ['user1@domain.ltd', 'user2@domain.ltd']

msg = MIMEText(sys.argv[2])
msg['Subject'] = sys.argv[1]
msg['From'] = sender
msg['To'] = ", ".join(recipients)

s = SMTP('mail.domain.ltd', 465)
s.set_debuglevel(False)
s.login("sender@domain.ltd","password")
s.sendmail(sender, recipients, msg.as_string())
s.quit()
