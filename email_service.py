#!/usr/bin/env python

# import smtplib
# from email.mime.text import MIMEText

# sender = 'admin@example.com'
# receivers = ['info@example.com']


# port = 25
# msg = MIMEText('This is test mail')

# msg['Subject'] = 'Test mail'
# msg['From'] = 'admin@example.com'
# msg['To'] = 'info@example.com'

# with smtplib.SMTP('localhost', port) as server:
    
#     # server.login('username', 'password')
#     server.sendmail(sender, receivers, msg.as_string())
#     print("Successfully sent email")


from smtplib import SMTP
from email.mime.multipart import MIMEMultipart

# By default the type is set to mixed
message = MIMEMultipart()
message["Subject"] = "Hello World"
message["From"] = "Anonimus <hello@gmail.com>"
message["To"] = "Reception <desert1988@gmail.com>"
# If a Reply-To is explicitly provided then the email client will
# use this address when the user hit the reply button 
message["Reply-To"] = "Support <different-address@gmail.com>"

smtp = SMTP("localhost", 25)
smtp.sendmail(message["From"], message["To"], encoded_email)
smtp.quit()

