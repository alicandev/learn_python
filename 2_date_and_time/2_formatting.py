from datetime import datetime
now = datetime.now()

### DATE FORMATTING ###
print("using predefined control codes")
# year: %y/%Y, weekday: %a/%A, month: %b/%B, day of month: %d
print(now.strftime("%a, %d %B, %y"))

print("\nlocale's date and time")
# date and time: %c, date: %x, time: %X
print(now.strftime("date and time: %c"))
print(now.strftime("date: %x"))
print(now.strftime("time: %X"))


## TIME FORMATTING
print("\nusing predefined control codes")
# 12/24hr: %I/%H, min: %M, sec: %S, am/pm: %p
print(now.strftime("current time: %I:%M:%S %p"))
print(now.strftime("24-hour time: %H:%M"))
