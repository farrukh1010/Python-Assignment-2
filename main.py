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

def count_vowels(s):
    
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


result = count_vowels("hello world")
print(result)  

