import datetime

from datetime import date
# module for time stamps
t = datetime.time(4,45,55)

print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(t.tzinfo)

today = datetime.date.today()

print(today)


# difference between two date objects

datetime1 = date(2021,11,3)
datetime2 = date(2020,11,3)

result = datetime1 - datetime2

print(result)

# datetime1 = datetime(2021,11,3,22,0)
# datetime2 = datetime(2020,11,3,12,0)
#
# result = datetime1 -datetime2
#
# print(result)