def my_function():
  print("Hello from a function")

my_function()

# arguments

def newFUnc(fname):
  print(fname + " Refsnes")

newFUnc("Emil")
newFUnc("Tobias")
newFUnc("Linus")




def ff(fname, lname):
  print(fname + " " + lname)

ff("Emil", "Refsnes")




def func(*kids):
  print("The youngest child is " + kids[2])
#    * is for unknown number of parameters

func("Emil", "Tobias", "Linus")


def func2(child3, child2, child1):
  print("The youngest child is " + child3)

func2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# kwargs

def func3(**kid):
  print("His last name is " + kid["lname"])

func3(fname = "Tobias", lname = "Refsnes")




def func4(country = "Norway"):
  print("I am from " + country)

func4("Sweden")
func4("India")
func4("Brazil")
func4()



def func5(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

func5(fruits)



def func6(x):
  return 5 * x

print(func6(3))
print(func6(5))
print(func6(9))


def f1():
  pass




def f2(x, /):
  print(x)

f2(3)


f2(x = 3) # error





# Keyword-Only Arguments

def f3(*, x):
  print(x)

f3(x = 3)





# def my_function(*, x):
#   print(x)

# my_function(3)

# error code




def f4(a, b, /, *, c, d):
  print(a + b + c + d)

f4(5, 6, c = 7, d = 8)

