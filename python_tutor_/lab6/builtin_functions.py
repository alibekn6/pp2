import math
import time

def multiply_numbers_in_list():
    a = [2, 3, 4]
    result = math.prod(a)
    print("Multiplication result:", result)


def count_upper_lower_letters():
    s = input("Enter a string: ")
    u = 0
    l = 0
    for c in s:
        if c.isupper():
            u += 1
        elif c.islower():
            l += 1
    print("Uppercase letters:", u)
    print("Lowercase letters:", l)


def check_palindrome():
    s = input("Enter a string to check for palindrome: ").strip()
    if s == s[::-1]:
        print("True (It's a palindrome)")
    else:
        print("False (It's not a palindrome)")


def square_root_after_milliseconds():
    x = int(input("Enter a number for square root: "))
    y = int(input("Enter milliseconds to wait: "))
    time.sleep(y / 1000)
    print(f"Square root of {x} after {y} milliseconds is {math.sqrt(x)}")


def check_tuple_elements():
    t = (True, True, True)
    print("All tuple elements are true:", all(t))


print("1. Multiply all numbers in a list:")
multiply_numbers_in_list()
print("\n2. Count upper and lower case letters:")
count_upper_lower_letters()
print("\n3. Check if a string is a palindrome:")
check_palindrome()
print("\n4. Square root after specific milliseconds:")
square_root_after_milliseconds()
print("\n5. Check if all elements of a tuple are true:")
check_tuple_elements()
