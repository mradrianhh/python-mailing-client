import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg["From"] = "hansen.adrian.hardy@gmail.com"
msg["To"] = "hansen.adrian.hardy@gmail.com"
msg["Subject"] = "Just a test"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

attachment = open("private.txt", "rb")

p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", "attachment; filename=private.txt")
msg.attach(p)

text = msg.as_string()

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls(context=context)
    smtp.login("hansen.adrian.hardy@gmail.com", "pappa123")
    smtp.sendmail("hansen.adrian.hardy@gmail.com", "hansen.adrian.hardy@gmail.com", text)