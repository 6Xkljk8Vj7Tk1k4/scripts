#!/usr/bin/env python
#
# Forward sms to mailbox using smtp
#
# cat /etc/gammu-smsdrc | grep RunOn
# RunOnReceive = /usr/bin/script.py
#
from __future__ import print_function
import os
import sys
import smtplib
from email.mime.text import MIMEText

def get_message():
    number = os.environ['SMS_1_NUMBER']

    numparts = int(os.environ['DECODED_PARTS'])
    if numparts:
        # Get all text parts
        text = ''
        for i in range(0, numparts):
            varname = 'DECODED_%d_TEXT' % i
            if varname in os.environ:
                text = text + os.environ[varname]
    else:
        text = os.environ['SMS_1_TEXT']

    text = text.decode('UTF-8')
    return number, text

number, text = get_message()

msg = MIMEText(text)
msg['Subject'] = 'New sms from %s' % number
msg['From'] = 'from@domain.ltd'
msg['To'] = 'to@domain.ltd'

s = smtplib.SMTP('mail.domain.ltd', 25)
s.login("from@domain.ltd","password")
s.sendmail('from@domain.ltd', 'to@domain.ltd', msg.as_string())
s.quit()
