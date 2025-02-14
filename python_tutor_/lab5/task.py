import re


with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()


def match_a_zero_or_more_b(text):
    return bool(re.search(r'ab*', text))


def match_a_two_to_three_b(text):
    return bool(re.search(r'ab{2,3}', text))


def find_lowercase_underscore_sequences(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

def find_uppercase_lowercase_sequences(text):
    return re.findall(r'[A-Z][a-z]+', text)


def match_a_anything_b(text):
    return bool(re.search(r'a.*b$', text))

def replace_space_comma_dot_with_colon(text):
    return re.sub(r'[ ,.]', ':', text)


def snake_to_camel(snake_str):
    return ''.join(word.title() for word in snake_str.split('_'))



def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)


def insert_spaces(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)


def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', camel_str).lower()



print(match_a_zero_or_more_b(text))

print(match_a_two_to_three_b(text))



print(find_lowercase_underscore_sequences(text))

print(find_uppercase_lowercase_sequences(text))

print(match_a_anything_b(text))

print(replace_space_comma_dot_with_colon(text))

print(snake_to_camel("hello_world_python"))

print(split_at_uppercase("HelloWorldPython"))

print(insert_spaces("HelloWorldPython"))

print(camel_to_snake("helloWorldPython"))

