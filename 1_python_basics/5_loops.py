print("THE WHILE LOOP")
x = 0
while (x < 5):
  print(x)
  x+=1

print("THE FOR ITERATOR")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days: 
  print(d)

print("BREAK AND CONTINUE STATEMENTS")
for x in range(5, 10):
  # if (x == 7): break
  if (x % 2 == 0): continue
  print(x)

print("THE ENUMERATE FUNCTION")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for (i, d) in enumerate(days):
  print(i, d)
