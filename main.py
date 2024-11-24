
    #  Basic Function Questions

# 1. Write a function to calculate the area of a circle given its radius.

# def calculate_circle_area(radius):
#     return 3.14159 * radius ** 2


# radius = float(input("Enter the radius of the circle: "))
# area = calculate_circle_area(radius)
# print(f"The area of the circle is: {area}")



# 2. Create a function that takes two numbers and returns their sum.
# def add_numbers(num1, num2):
  
#     return num1 + num2


# result = add_numbers(5, 3)
# print(f"The sum is: {result}")



# 3. Write a function to find the factorial of a number using recursion.

# def factorial(n):
    
#     if n == 0 or n == 1: 
#         return 1
#     return n * factorial(n - 1) 


# print(factorial(5)) 





# 4. Write a function that takes a string and returns it reversed.

# def reverse_string(s):
  
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str


# result = reverse_string("hello")
# print(result) 





# 5. Create a function to check if a given number is prime.

# def is_prime(number):
   
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True


# print(is_prime(7)) 
# print(is_prime(10))  



# 6. Write a function to count the vowels in a given string.

# def count_vowels(s):
    
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count


# result = count_vowels("hello world")
# print(result)  

# Intermediate Function Questions

# 1. Create a function that takes a list of numbers and returns the largest number.

# def find_largest_number(numbers):
  
#     if not numbers:  
#         return None
#     largest = numbers[0]  
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest


# result = find_largest_number([3, 1, 4, 1, 5, 9, 2, 6])
# print(result)  




# 2. Write a function to find the nth Fibonacci number using recursion.

# def fibonacci(n):
    
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5)) 


# 3. Write a function to check whether a string is a palindrome.

# def is_palindrome(s):
#     s = s.lower() 
#     return s == s[::-1]  

# print(is_palindrome("radar")) 
# print(is_palindrome("hello"))  
# print(is_palindrome("Madam"))  


# 4. Create a function that takes a list of integers and returns the sum of all even numbers.
# def sum_of_evens(numbers):
#     evens = [num for num in numbers if num % 2 == 0]  
#     if not evens:  
#         return " Sorry, No even number is found"
#     return sum(evens)


# print(sum_of_evens([1, 2, 3, 4, 5, 6]))  
# print(sum_of_evens([7, 11, 13]))        
# print(sum_of_evens([10, 20, 30]))        


# 5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.
# def gcd(a, b):
#     while b != 0:  # Keep going until b becomes 0
#         a, b = b, a % b  # Update a to b, and b to the remainder
#     return a  # When b is 0, a is the GCD
  

 
# print(gcd(48, 18))  
# print(gcd(56, 98))  




# 6. Create a function that accepts a dictionary and returns the key with the highest value.

# def key_with_highest_value(d):
#     return max(d, key=d.get) if d else "Dictionary is empty"
# data = {'a': 10, 'b': 25, 'c': 5}
# print(key_with_highest_value(data)) 


# Advanced Function Questions

# 1. Write a function that calculates the power of a number without using the ** operator.

# def power(base, exponent):
#     # Handle edge case for exponent 0
#     if exponent == 0:
#         return 1
    
#     # Handle negative exponents
#     is_negative = exponent < 0
#     exponent = abs(exponent)
    
#     # Perform iterative multiplication
#     result = 1
#     for _ in range(exponent):
#         result *= base
    
  
#     if is_negative:
#         return 1 / result
    
#     return result


# print(power(2, 3))  
# print(power(5, -2)) 
# print(power(7, 0))  



# 2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

# def convert_temperature(value, scale):
#     if scale.upper() == "F":
#         return value * 9/5 + 32  # Celsius to Fahrenheit
#     if scale.upper() == "C":
#         return (value - 32) * 5/9  # Fahrenheit to Celsius
#     raise ValueError("Invalid scale. Use 'C' or 'F'.")


# print(convert_temperature(25, "F")) 
# print(convert_temperature(77, "C"))  



# 3. Write a function to flatten a nested list.

# def flatten(nested_list):
#     """
#     Flattens a nested list into a single list.

#     Parameters:
#         nested_list (list): A list that may contain nested lists.

#     Returns:
#         list: A flattened version of the input list.
#     """
#     result = []
#     for item in nested_list:
#         if isinstance(item, list):
#             result.extend(flatten(item))  # Recursively flatten
#         else:
#             result.append(item)  # Add non-list items
#     return result


# nested = [1, [2, [3, 4], 5], [6, 7], 8]
# print(flatten(nested)) 



# 4. Create a function to check if two strings are anagrams.

# def are_anagrams(str1, str2):
#     """
#     Check if two strings are anagrams.

#     Parameters:
#         str1 (str): The first string.
#         str2 (str): The second string.

#     Returns:
#         bool: True if the strings are anagrams, False otherwise.
#     """
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
#     # Check if sorted characters are the same
#     return sorted(str1) == sorted(str2)


# print(are_anagrams("listen", "silent"))  
# print(are_anagrams("hello", "world"))    


# 5. Write a function that takes a list and removes all duplicate elements.

# def remove_duplicates(lst):
#     """
#     Removes duplicates from a list while maintaining the order.

#     Parameters:
#         lst (list): The input list.

#     Returns:
#         list: A list with duplicates removed.
#     """
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result


# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  


# 6. Create a function that takes a string and counts the frequency of each character.

# def count_character_frequencies(s):
#     frequency = {}
#     for char in s:
#         frequency[char] = frequency.get(char, 0) + 1
#     return frequency


# example_string = "hello world"
# result = count_character_frequencies(example_string)
# print(result)




# Real-world Scenarios

# 1. Write a function that takes a list of employee salaries and calculates the average salary.

# def average_salary(salaries):
#     """
#     Calculates the average salary.

#     Parameters:
#         salaries (list): A list of employee salaries (numbers).

#     Returns:
#         float: The average salary, or 0 if the list is empty.
#     """
#     if not salaries:
#         return 0  # Return 0 if the list is empty
#     return sum(salaries) / len(salaries)


# salaries = [50000, 60000, 55000, 70000]
# print(average_salary(salaries))  


# 2. Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters.

import random
import string

def generate_random_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    
    # Ensure at least one character from each category
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    
   
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    
    return ''.join(password)


try:
    length = int(input("Enter the desired password length (minimum 4): "))
    print("Generated Password:", generate_random_password(length))
except ValueError:
    print("Please enter a valid number.")


