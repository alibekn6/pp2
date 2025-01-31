mylist = ["apple", "banana", "cherry"]


thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

print(thislist[1])
print(thislist[-1])

print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])


print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")





thislist[1:3] = ["watermelon"]
print(thislist)




thislist.insert(2, "watermelon")
print(thislist)



thislist.append("orange")
print(thislist)


thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist



thislist.clear()
print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


for i in range(len(thislist)):
  print(thislist[i])


i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


[print(x) for x in thislist]






fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


newlist = [x for x in fruits if "a" in x]

print(newlist)


newlist = [x for x in fruits if x != "apple"]


newlist = [x for x in fruits]

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist.sort(key = str.lower)
print(thislist)

thislist.reverse()
print(thislist)

mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)


mylist = thislist[:]
print(mylist)


# join two lists


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)

print(list1)


list1.extend(list2)
print(list1)
