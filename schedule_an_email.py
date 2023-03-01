# This file shows you how to schedule an email to send at a certain time in Python using Google Gmail

from sending_emails_in_python import send_email_gmail
import datetime as dt
import time

# First, define the variables message, title_email, password, from_email, to_email. 
# You can find a description of each one in the file "sending_emails_in_python.py".

# Second, specify the time (insert the arguments with your preference)
send_time = dt.datetime(<year>, <month>, <day>, <hour>, <minute>, <second>) 

# use time.sleep() to call send_email_gmail() periodically
time.sleep(send_time.timestamp() - time.time())

# Finally, send the email (insert the arguments with your preference)
send_email_gmail(<message>, <title_email>, <password>, <from_email>, <to_email>)
