import os
import smtplib

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASS = os.environ.get('MY_PASS')
RECIPIENTS = os.environ.get('RECIPIENTS')


def send_email(msg):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENTS, msg='Subject: New message from my blog\n\n'
                                                                         f'{msg}')
