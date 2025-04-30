from datetime import datetime
from datetime import timedelta
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        # create local datetime object.
        date_time = datetime.now()
        print("{0}\t{1}\t{2}".format(item, cost, date_time))


# Add 1 day
time1 = datetime.now() + timedelta(days=1)
print(time1)
# Subtract 60 seconds from prior
time2 = time1 - timedelta(seconds=60)
print(time2)
# Add 2 years from prior
time3 = time2 + timedelta(days=730)
print(time3)

# datetime object 100 days, 10 hours, 13 minutes
timeobject = timedelta(days=100, hours=10, minutes=13)
print(timeobject)

# create datetime object
datetime_object = datetime.now()
print(datetime_object)
print('Type :- ', type(datetime_object))

height_list = []


def height_calendar():
    """requests height measurements and returns height and time to list"""
    date = datetime_object.date()
    feet, inches = input("Enter your height in feet and inches (seperated by a space): ").split()
    print(f"On {date} you were {feet}' {inches}'' tall")
    height_list.append((date, feet, inches))


height_calendar()
print(height_list)
