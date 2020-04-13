#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import os
import smtplib
import imghdr
from email.message import EmailMessage
from datetime import datetime


def send_email(from_addr, gmail_key,
               to_addrs, subject,
               body_txt='DEFAULT - This is a plain text email',
               body_html=None, attached_file=None):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addrs

        msg.set_content(body_txt)  # Body as text

        if body_html is not None:
            msg.add_alternative(body_html, subtype='html')  # Body as HTML

        # if attached_file == None:
        #     pass
        # else:
        #     with open(attached_file, 'rb') as f:
        #         file_date = f.read()
        #         file_type = imghdr.what(f.name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_addr, gmail_key)
            smtp.send_message(msg)
            print('Email sent successfully')

    except Exception as e:
        print(e)
        print('\nEmail failed to send.')


from_addr = os.environ.get('EMAIL_USER')
gmail_key = os.environ.get('EMAIL_PASS')

to_addrs = ['test@test.com', 'me-myself-and-i@exemple.com']

subject = f'Python Email Sender bot - TEST - \
{datetime.now().strftime("%A, %d. %B %Y %I:%M%p")}'

msg = """This email has been sent by a Python Bot!
Still have to find how to send attached files.
"""

body_html = """<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        <p>Still have to figure out the attach file thingy....</p>
    </body>
</html>"""


if __name__ == "__main__":
    # send_email(from_addr, gmail_key, to_addrs,
    #            subject, body_html=body_html)
    send_email(from_addr, gmail_key, to_addrs,
               subject, msg, body_html)
    # send_email(from_addr, gmail_key, to_addrs,
    #            subject, msg)
