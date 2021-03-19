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

c = myClass()
c.method1()
c.method2('foo')

c2 = anotherClass()
c2.method1()
c2.method2('bar')