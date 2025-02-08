# 1
def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(100))


# 2
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

print(fahrenheit_to_celsius(100))

# 3

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return "No solution"

print(solve(35, 94))


# 4
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

print(filter_prime([10, 3, 7, 12, 19, 4, 5, 13])) 

# 5
from itertools import permutations


def string_permutations(s):
    for perm in permutations(s):
        print(''.join(perm))

string_permutations("abc")

# 6
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_sentence("We are ready"))

# 7

def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums)-1))

print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False


# 8

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False

# 9

import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

print(sphere_volume(3))

# 10
def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_list([1, 2, 2, 3, 4, 4, 5])) 

# 11

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello")) # false



# 12

def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])


# 13

import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    attempts = 0
    while True:
        guess = int(input("Take a guess.\n"))
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break



from scsc import grams_to_ounces, filter_prime

print(grams_to_ounces(100))  # Convert 100 grams to ounces
print(filter_prime([10, 3, 7, 12, 19, 4, 5, 13]))  # Get prime numbers

