import calendar

print("\ncreate a plaintext calendar")
c = calendar.TextCalendar(calendar.MONDAY)
print(c.formatmonth(2017, 1, 0, 0))

print("\ncreate an HTML formatted calendar")
hc = calendar.HTMLCalendar(calendar.MONDAY)
print(hc.formatmonth(2017, 1))


print("\nloop over the days of a month")
for i in c.itermonthdays(2017,8): print(i)

print("\nprinting month names")
for name in calendar.month_name: print(name)

print("\nprinting day names")
for name in calendar.day_name: print(name)


print("\ncalculate days based on a rule")
# team meetings are going to be on every first Friday of the month
print("team meetings are going to be on: ")
for m in range(1, 13):
  mc = calendar.monthcalendar(2018, m)
  week_one = mc[0]
  week_two = mc[1]

  # remember: 0s in calendars mean the day belongs to another month
  if week_one[calendar.FRIDAY] != 0:
    meet_day = week_one[calendar.FRIDAY]
  else:
    meet_day = week_two[calendar.FRIDAY]

  print("%10s %2d" % (calendar.month_name[m], meet_day))




