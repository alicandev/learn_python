# defining a class with methods
class myClass():
  def method1(self): 
    print('myClass.method1')

  def method2(self, text):
    print('myClass.method2 ' + text)
  
  # defining a class that inherits another class
class anotherClass(myClass):
  def method1(self): 
    myClass.method1(self)

  def method2(self, text):
    print('anotherClass.method2 ' + text)

o = myClass()
o.method1()
o.method2('foo')

o2 = anotherClass()
o2.method1()
o2.method2('bar')