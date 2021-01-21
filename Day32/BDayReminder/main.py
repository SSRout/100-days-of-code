# 1.import required packages
from datetime import datetime
import pandas
import random
import smtplib
# 2.calculate todays date and csv data
today=datetime.now()
today_tuple=(today.month,today.day)
data=pandas.read_csv("Day32/BDayReminder/birthdays.csv")
MY_EMAIL = "test mail id"
MY_PASSWORD = "testkey"
# 3. create dictionary
birtdays_dict={(data_row["month"],data_row["day"]): data_row for(index,data_row) in data.iterrows()}

# 4. compare todays date with dictionary
if today_tuple in birtdays_dict:
    birthday_person=birtdays_dict[today_tuple]
    file_path=f"Day32/BDayReminder/letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as template:
        context=template.read()
        context=context.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(MY_EMAIL,MY_PASSWORD)
        con.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{context}"
        )

    # 5.
    # Schedule it  on cloud
    # https://www.pythonanywhere.com/





