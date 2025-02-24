import smtplib
from email_pass import my_email, password
import datetime as dt
import random


RECEIVER_ADDRESS = ""
DAY_OF_WEEK = dt.datetime.now().weekday()

if DAY_OF_WEEK == 0:

    with open("quotes.txt", "r") as file:
        file_contents = file.readlines()
        quote = random.choice(file_contents)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=RECEIVER_ADDRESS,
            msg=f"Subject:Monday Motivation\n\n"
                f"{quote}"
        )
