#!/usr/bin/python
import smtplib, base64, time
#userName = base64.encodestring('username').strip()
#password = base64.encodestring('password').strip()
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)

smtp.connect("127.0.0.1:25")

#msg = ("From: hzy@nttlog.com\r\nMessage-ID: <eeeaaaaaaaaaaaaaaaaaaaaaaaaaaaac@bb.com>\r\nTo: hzyyollow@gmail.com\r\n\r\n")
smtp.ehlo()
smtp.starttls() #554 5.5.1 Error: TLS already active
#smtp.helo()
#time.sleep(30)
#smtp.ehlo()
smtp.sendmail('hzy@aa.com','hzy@eric-stg-clp1.hes20.net','X-TESTCASEID:MF-0010\r\nThis is test tls email for gmail')
#time.sleep(2)
smtp.quit()