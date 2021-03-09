# basic function
def printFoo():
  print('foo')

# function that takes parameters
def concat(txt1, txt2):
  print(txt1, ' ', txt2)

# function that returns a value
def add(num1, num2):
  return num1 + num2

# function with default value for its argument
def multiply(num1, num2 = 1):
  return num1 * num2

# function with indefinite number of arguments
def multi_add(*args):
  result = 0
  for x in args:
    result += x
  return result

printFoo()
concat('foo', 'bar')
print(add(3, 3))
print(multiply(3))
print(multiply(3, 3))
print(multi_add(1, 3, 4, 4, 6))