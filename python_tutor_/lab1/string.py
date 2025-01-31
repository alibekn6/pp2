print("Hello")
print('Hello')




print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')




a = "Hello"
print(a)



a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



a = "Hello, World!"
print(a[1])




for x in "banana":
  print(x)



a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)




txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")




txt = "The best things in life are free!"
print("expensive" not in txt)



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
        








# slicing



b = "Hello, World!"
print(b[2:5])


b = "Hello, World!"
print(b[:5])


b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])




# modify strings


a = "Hello, World!"
print(a.upper())




a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"



a = "Hello, World!"
print(a.replace("H", "J"))


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)




# format

age = 36
txt = "My name is John, I am " + age
print(txt)


age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)




# error
# txt = "We are the so-called "Vikings" from the north."  

txt = "We are the so-called \"Vikings\" from the north."




# string methods

s = "some string"
s.capitalize()
s.casefold()
s.center()
s.count('o')
s.encode()
s.endswith()
s.expandtabs()
s.find('e')
s.format()
s.islower()
s.isupper()
s.isalnum()
s.isalpha()
s.isdigit()
s.isnumeric()
s.isprintable()
s.istitle()
s.lstrip()
