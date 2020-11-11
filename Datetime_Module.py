import datetime

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