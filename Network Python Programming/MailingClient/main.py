# not twerking yet

# import smtpd
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
# your smtp account
server = smtplib.SMTP('smtp.****.com', 25)

server.ehlo()
# password file for you email account, create a password.txt file, encode it, decode it here then read
with open('password.txt', 'r') as f:
    password = f.read()
# you email account
server.login('', password)

msg = MIMEMultipart()
msg['From'] = 'Mad-M'
# your test mail account
msg['To'] = ''
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attatchemnt; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('yoursmtpmail', 'yourtestmail', text)
