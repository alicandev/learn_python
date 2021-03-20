from datetime import date
from datetime import datetime
# above lines basically tell python to import date and
# datetime classes from the built-in datetime module

## THE DATE OBJECT
# get today's date
today = date.today()

# print today's date as is
print("Today's date is", today)

# print out today's individual components
print("Date components:", today.day, today.month, today.year)

# print today's weekday number
print("Today's weekday number is", today.weekday())

# use weekday number as an index to to find an item
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
print("Like I said – today is", days[today.weekday()])

## THE DATETIME OBJECT
# get today's date from the datetime class
today = datetime.now()
print("The current date and time is", today)

# get the current time
t = datetime.time(datetime.now()) # notice that it takes a datetime object
print(t)