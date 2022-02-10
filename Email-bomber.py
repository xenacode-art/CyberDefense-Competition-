import smtplib

subject = 'Python Email'
body = 'this email was sent with python'
message = f'Subject: {subject}\n\n{body}'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("username", "password")
i = 1
while i < 11:
    server.sendmail("from email address", "to email address", message)
    i += 1
server.quit()
