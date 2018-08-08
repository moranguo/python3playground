#! /usr/bin/python
import smtplib, base64, time
from email.message import Message
from email.header import Header
#userName = base64.encodestring('from').strip()
#password = base64.encodestring('password').strip()
smtp = smtplib.SMTP()
#smtp.set_debuglevel(1)
#SJDC
smtp.connect("127.0.0.1:25")

sender='test@bb.com'
rcpt = 'hzy@eric-stg-xsp1.hes20.net'
msg = Message()
h = Header("abc\rdef\r\naggg\nkkk1<2>3&4'5\"6", 'utf-8')
msg['Subject'] = h
msg['From'] = sender
msg['To'] = rcpt
#
smtp.ehlo()
smtp.sendmail(sender,rcpt,msg.as_string())
#
print(h)
print(msg.as_string())

smtp.quit()
