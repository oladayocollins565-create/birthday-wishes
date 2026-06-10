import smtplib
import pandas as pd
import datetime as dt
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

#Reading the csv file contain the information of the birthday person
csv = pd.read_csv("birthdays.csv")
birthday_dict = {(row["month"], row["day"]):row.to_dict() for (index, row) in csv.iterrows()}

#Making  birthday variable to keep a tuple of the present month and day
now = dt.datetime.now()
month = now.month
day = now.day
birthday = (month, day)

# Creating a if statement to known if today is someone birthday.
if birthday in birthday_dict:
    birthday_person = birthday_dict[birthday]
    # Opening and randomizing the letter files
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        content = file.read()
        new_letter = content.replace("[NAME]", birthday_person["name"])

    #Sending the birthday message to the person mail.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                             msg=f"Subject:Birthday Wishes\n\n{new_letter}"
                            )
        connection.close()






