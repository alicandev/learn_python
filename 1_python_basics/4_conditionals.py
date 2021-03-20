x, y = 100, 100

# conditional flow
if (x < y):
  st = "x is less than y"
elif (x > y):
  st = "x is greater than y"
else:
  st = "x equals y"

print(st)

# conditional statements
st = "x is less than y" if (x < y) else "x is greater than or equal to y"

print(st)