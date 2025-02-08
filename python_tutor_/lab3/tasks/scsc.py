def grams_to_ounces(grams):
    return 28.3495231 * grams

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]