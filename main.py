
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


