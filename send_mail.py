from email import message
import smtplib
import os
from email.mime.text import MIMEText

# def send_mail(name, phone, email, comments):
#     port = 2525
#     smtp_server = 'smtp.mailtrap.io'
#     login = 'b37a81e73f2874'
#     password = '5d1fa2dd3edcd1'
#     message = f"<h3>New Contact Me Submission</h3><ul><li>Name: {name}</li><li>Phone: {phone}</li><li>Email: {email}</li><li>Comments: {comments}</li></ul>"
#     sender_email = 'ex1@gmail.com'
#     receiver_email = 'ex2@gmail.com'
#     ms g = MIMEText(message, 'html')
#     msg['Subject'] = 'Contact Me'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email

#     # Send email
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(login, password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())

EMAIL_PWD = os.environ.get('GMAIL_PWD')
def send_mail(name, phone, email, comments):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('lalalolo.2469@gmail.com', EMAIL_PWD)

        message = f"<h3>New Contact Me Submission</h3><ul><li>Name: {name}</li><li>Phone: {phone}</li><li>Email: {email}</li><li>Comments: {comments}</li></ul>"

        msg = MIMEText(message, 'html')
        msg['Subject'] = 'Contact Me'
        msg['From'] = 'lalalolo.2469@gmail.com'
        msg['To'] = 'lalalolo.2469@gmail.com'

        smtp.sendmail('lalalolo.2469@gmail.com', 'lalalolo.2469@gmail.com', msg.as_string())