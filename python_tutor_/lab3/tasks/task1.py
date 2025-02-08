# 1

class StringHandler:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

# Example Usage:
handler = StringHandler()
handler.getString()
handler.printString()



# 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Example Usage:
sq = Square(5)
print(sq.area())  # Output: 25



# 3

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example Usage:
rect = Rectangle(4, 6)
print(rect.area())  # Output: 24


# 4

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example Usage:
p1 = Point(2, 3)
p2 = Point(5, 7)
p1.show()  
p1.move(4, 6)
p1.show()
print(p1.dist(p2))  # Output: Distance between points


# 5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")

# Example Usage:
acc = Account("John Doe", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)  # Should print "Insufficient balance!"
