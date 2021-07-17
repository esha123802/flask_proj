from email import message
import smtplib
from email.mime.text import MIMEText

def send_mail(name, phone, email, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'b37a81e73f2874'
    password = '5d1fa2dd3edcd1'
    message = f"<h3>New Contact Me Submission</h3><ul><li>Name: {name}</li><li>Phone: {phone}</li><li>Email: {email}</li><li>Comments: {comments}</li></ul>"
    sender_email = 'ex1@gmail.com'
    receiver_email = 'ex2@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Contact Me'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

