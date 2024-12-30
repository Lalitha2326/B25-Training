"""
Author : GOVIND
Date   : 10-12-2024
"""


"""
lambda/anonymous function:
--------------------------

lambda arguments: expression
any number of args but a single expression

"""

print("\n")
# Lambda function adding two numbers
# add = lambda x, y: x + y
# print("Lambda function with multiple arguments: ", add(3, 7))
# print("\n****************************************************************************\n")
#
# # Lambda function calculating the product of three numbers
# multiply_three = lambda x, y, z: x * y * z
# print("Lambda function with a complex expression: ", multiply_three(2, 3, 4))
# print("\n****************************************************************************\n")
#
# # Sorting a list of tuples based on the second element using lambda
# data = [(1, 5), (3, 2), (2, 8)]
# sorted_data = sorted(data, key=lambda x: x[1])
# print("Using lambda with built-in functions: ", sorted_data)
# print("\n****************************************************************************\n")
#
# # Using zip to combine two lists into pairs
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# zipped_data = zip(names, ages)
# print("\n******************** zip ********************\n")
# print("zipped_data", zipped_data)
# print(list(zipped_data))
# print(dict(zipped_data))
# print(set(zipped_data))
# print(tuple(zipped_data))
# print(str(zipped_data))


# Using map to square each element in a list
numbers = (1, 2, 3, 4)
squared_numbers = map(lambda x: x ** 2, numbers)
print("\n******************** map ********************\n")
# print("squared_numbers = ", squared_numbers)
print(list(squared_numbers))
# print(dict(squared_numbers))
# print(set(squared_numbers))
# print(tuple(squared_numbers))
# print(str(squared_numbers))


# Using filter to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("\n******************** filter ********************\n")
print(list(even_numbers))
print(dict(even_numbers), "******************")
# print(set(even_numbers))
# print(tuple(even_numbers))
# print(str(even_numbers))


# Using reduce to find the product of all elements in a list
from functools import reduce

numbers = [240, 7, 2, 2]
product = reduce(lambda x, y: x * y, numbers)
print("\n******************** reduce ********************\n")
print(product)
