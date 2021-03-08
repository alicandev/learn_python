# declare a variable and initalise it
f = 0
print(f)

# re-declaring the variable works
f = "foo"
print(f)

# variables of different types cannot be combined
print("this is a string " + str(123))

# global vs local variables in functions
def someFunc():
  f="bar"
  print(f)

someFunc()
print(f)

# delete the definition of a variable
del f
print(f)