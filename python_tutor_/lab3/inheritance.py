class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



x = Person("John", "Doe")
x.printname()



class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


w = Student("Mike", "Olsen", 2019)
w.printname()
w.welcome()


# Mike Olsen
# functions from parent are avaliable

