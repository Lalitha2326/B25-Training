"""
Author : GOVIND
Date   : 09-12-2024
"""
"""
req:

procedural    - input()

functional    - def function_name(identifier)(params(optional)):
                    block of code


oop

functions methods(.)
print return
parameters arguments
positional args, keyword args
params without default, params with default
*args **kwargs

string formats - f-strings , old style %s %d %f, .format()
"""

# 'add two numbers'
# n1 = input("enter first number n1: ")
# n2 = input("enter second number n2: ")
#
# res = n1 + n2
# print(res)
#
# 'multiply two numbers'
# n3 = input("enter first number n3: ")
# n4 = input("enter second number n4: ")
#
# res2 = n3 + n4
# print(res2)

# def add_two_numbers(n1, n2):
#     res = n1 + n2
#     # print(res)
#     return res
#
# def multiply_two_numbers(n3, n4):
#     res = n3 * n4
#     x = add_two_numbers(15, 30)
#     # print(res + x)
#     return res + x
#
# # add_two_numbers(15, 30)
#
# # multiply_two_numbers(5, 2)
# # x = 45
# y = multiply_two_numbers(5, 2)
# print(y)

# def hello(name):
#     return f"from hello function {name}"
# print(hello("suresh"))

# def emp_data(name, age, sal=5000):
#     return f"name is {name}, age is {age}, salary is {sal}"

# res = emp_data("ramesh", 25, 25986.3)
# res = emp_data(25, "ramesh", 25693.3)
# res = emp_data(sal=258000, name="suresh", age=20)
# res = emp_data("ramesh", 20, sal=250000)
# print(res)

# res = emp_data("ramesh", 25)
# res = emp_data("ramesh", 25, 25000)
# print(res)

# def demo():
#     print("hello")
#     print("hi")
#     print("python")
#
# demo()

# def demo():
#     return "hello"
#     return "hi"
#     return "python"
#
# res = demo()
# print(res)

# def minor_major(age):
#     if age >= 18:
#         return "major"
#     return "minor"
#     # else:
#     #     return "minor"
#
# res = minor_major(5)
# print(res)

# def demo(ls):
#     for each in [10, 20, 30, 40]:
#         return each
#
# res = demo([10, 20, 30, 40])
# print(res)
"""
ls = [10, 20, 30, 40]
for each in [10, 20, 30, 40]:
    return 10
"""

'add the given numbers'

# def add_numbers(*args):
#     sum = 0
#     for each in args:
#         sum+=each
#     return sum
#     # return f"{args}, {type(args)}"
#
# # res  =add_numbers()
# # res  =add_numbers(10)
# res  =add_numbers(10, 20, 30, 40)
# print(res)


# def key_word_args(**kwargs):
#     return f"{kwargs}, {type(kwargs)}"
#
# # res = key_word_args()
# res = key_word_args(name="ramesh", age=25, salary=250000)
# print(res)

# def args_kwargs(*args, **kwargs):
#     return (f"*args   : {args}, type: {type(args)}\n"
#             f"*kwargs : {kwargs}, type: {type(kwargs)}")
#
# # res = args_kwargs()
# res = args_kwargs(10, 20, 30, 40, name="ramesh", age=25, sal=25633)
# print(res)

# def demo(x, y, z, p, q):
#     return x, y, z, p, q
#
# res = demo(10, 20, 30, 40, 50)
# print(res, type(res))

# def emp_data(name, age, sal):
#     return name, age, sal
#
# # res = emp_data("ramesh", 25, 250000)
# # print(res)
#
# x, y, z = emp_data("ramesh", 25, 25000)
# print(x)
# print(y)

# def demo(p, q, r):
#     if p > 0:
#         return p, q, r
#     return q, r
#
# a = demo(-10, 20, 30)
# print(a)
# print(b)
# print(c)

