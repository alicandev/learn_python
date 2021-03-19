from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print('a basic timedelta')
print(timedelta(days=365,hours=5,minutes=1))
print('\n')

print('today\'s date')
now = datetime.now()
print(f'today is: {str(now)}')
print('\n')

print('one year from now')
print(str(now + timedelta(days=365)))
print('\n')

print('3 weeks and 2 days from now')
print(str(now + timedelta(weeks=3,days=2)))
print('\n')
print('\n 1 week ago today')
print((now - timedelta(weeks=1)).strftime('%A %B %d, %Y'))
print('\n')

print('days until the April Fools\' day')
today = date.today()
afd = date(today.year, 4, 1)
if afd < today:
  print(f'April Fools\' day already wen by {(today - afd).days} days ago')
  afd = afd.replace(year = today.year + 1)
time_to_afd = afd - today
print(f'It\'s just {time_to_afd.days} days until April Fools\' day')