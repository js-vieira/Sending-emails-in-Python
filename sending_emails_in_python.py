# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:07:33 2023

@author: Joana Vieira (js.vieira@campus.fct.unl.pt)
"""
# FOR PASSWORD
# 1. Go to https://myaccount.google.com/?hl=en&utm_source=OGB&utm_medium=act&nlr=1
# 2. Go to the security section and make sure that your 2-step verification is on in "Sign in to Google".
# 3. Then go to App password in "Sign in to Google". 
# 4. Select app = Other. Then it will ask you to Select the app and device you want to generate the app password for,
#    set it to the website, and Click on Generate. It will generate a password.
# 5. Copy the password and use this password for sending emails.


# Packages: 
import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email_gmail(message, title_email, password, from_email, to_email):
    
    """ 
    message = "message"
    password = "password obtained with the steps above"
    from_email = "your email"
    to_email = [list of emails]
    title_email = "title of email"
    """
    
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = ", ".join(to_email)
    msg['Subject'] = title_email
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], to_email, msg.as_string())
    print('Your email was sent! :)')
    server.quit()
    





