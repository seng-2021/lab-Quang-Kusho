import datetime
import calendar
from datetime import datetime as dt

def get_time():
    datetime_str = input("Enter the date and time in the format 'dd.mm.yyyy hh:mm': \n")
    datetime_object = dt.strptime(datetime_str, '%d.%m.%Y %H:%M')
    for i in ["year", "month", "day", "hour", "minute"]:
        print("You gave year " + str(eval(f"datetime_object.{i}")))

def cal_age():
    birthday_str = input("Enter your birthday as dd.mm.yyyy:\n")
    birthday_object = dt.strptime(birthday_str, '%d.%m.%Y')
    birthday_object = birthday_object.date()
    today_object = dt.today()
    today_object = today_object.date()
    month = datetime.date.today().strftime("%B")
    print(f"On {month} {today_object.day}, {today_object.year}, you were {(today_object - birthday_object).days} days old.")

def get_weekday():
    for i in range(7):
        print(calendar.day_name[i])

def get_month():
    for i in range(12):
        print((calendar.month_name[i+1])[:3])