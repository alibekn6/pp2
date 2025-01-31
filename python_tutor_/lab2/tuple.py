mytuple = ("apple", "banana", "cherry")
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)



tuple1 = ("abc", 34, True, 40, "male")
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

print(thistuple[-4:-1])

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


y = ("orange",)
thistuple += y

print(thistuple)


y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

del thistuple
print(thistuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

(green, yellow, *red) = fruits
# * rest of them

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

