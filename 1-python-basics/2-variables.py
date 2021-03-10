# declaring and initialising a variable
f = 0
print(f)

# re-declaring the variable
f = 'foo'
print(f)

# variables of different types cannot be combined
print('This is a string ' + str(123))

# global vs local variables in functions
def someFunc():
  f='bar'
  print(f)

someFunc()
print(f)

# deleting the definition of a variable
del f
print(f)