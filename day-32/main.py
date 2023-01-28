# import smtplib

# my_email = "bolivaral@gmail.com"
# password = "yaaryyvglulruqrw"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="linkagainsthungertranslation@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
print(type(month))
day_of_week = now.weekday()
month = now.month
print(day_of_week, month, year)

date_of_birth = dt.datetime(year=1972, month=8, day=10)
print(date_of_birth)