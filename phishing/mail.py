#!/usr/bin/env python3

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message_flag = "plain"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['From'] = input("From Name:") + ' <' + input("From Address:") + '> '
msg['To'] = input("To:")
msg['CC'] = input("CC:")
msg['BCC'] = input("BCC:")
msg['Subject'] = input("Subject:")
highpri = input("Flag this message/s as high priority? [yes|no]")
if not "yes" in highpri:
	prioflag1 = ""
	prioflag2 = ""
else:
	prioflag1 = ' 1 (Highest)'
	prioflag2 = ' High'
msg['X-Priority'] = prioflag1
msg['X-MSMail-Priority'] = prioflag2
try:
	html_flag = input("Send the message as html or plain? 'h' or 'p' [p]:")
	if html_flag == "" or html_flag == "p":
		message_flag = "plain"
	if html_flag == "h":
		message_flag = "html"
except KeyboardInterrupt:
            pass


# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
body = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>This mail is from my program.
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
#part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
#msg.attach(part2)

mesg = MIMEText(body, message_flag)
msg.attach(mesg)


# Send the message via SMTP server.
s = smtplib.SMTP('mail.smtp2go.com', 2525)
s.ehlo()
s.starttls()
s.login(username, password)
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
print("Mail sent successfully.")
