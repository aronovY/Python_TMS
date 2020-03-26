import datetime


year = int(input('Enter year'))
month = int(input('Enter month'))
day = int(input('Enter day'))
date = datetime.datetime(year, month, day, 0, 0, 0)
now = datetime.datetime.now()
print(now - date)