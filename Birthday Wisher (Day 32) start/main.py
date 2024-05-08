import random
import smtplib
import datetime as dt

MY_EMAIL = "yumpom306@gmail.com"
MY_PASSWORD = "xxxx" #Put your apppassword from gamil here

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
















# import smtplib
#
# my_email = "yumpom306@gmail.com"
# password = "zcbnwfljubgqnalt"
#
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="sessegnon.stephane48@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()  # This get the current date and time
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=2000, month=6, day=9, hour=2)
# print(date_of_birth)
