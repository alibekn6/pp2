# OOP


class MyClass:
  x = 5


p1 = MyClass()
print(p1.x) # 5





# init

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name) #John 
print(p1.age) # 35




class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p2 = Person2("John", 36)

print(p2) # John(36)





class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p3 = Person3("John", 36)
p3.myfunc()
# Hello my name is John



class Person4:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p4 = Person4("John", 36)
p4.myfunc()
# the same


p4.age = 33
del p4.age

p4.myfunc()

del p4


class Person:
  pass


