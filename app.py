#!/usr/bin/env python3

#function add numbers
def add_numbers(num1, num2):
    return num1 + num2

#function is_even
def is_even(number):
    return number % 2 == 0

#function reverse string
def reverse_string(text):
    return text[::-1]

#function count_vowels
def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()  
    count = sum(1 for char in text if char in vowels)
    return count


#function calculate_factorial
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input should be a non-negative number.")
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


#function apply decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)


#function sort list
def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])


#merge dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  
        else:
            merged_dict[key] = value  
    return merged_dict

#class creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")
