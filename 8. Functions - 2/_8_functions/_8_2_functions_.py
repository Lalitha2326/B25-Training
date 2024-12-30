"""
Author : GOVIND
Date   : 10-12-2024
"""
"""
functions

def function_name(params(optional)):
    block of code
    
function method
print return
params args
positional args  keyword args
params without default params with default
*args **kwargs

isinstance
stack memory
LEGB
nested recursive decorator
lambda
** typing module pydantic 
"""
#
# def multiply_by_five(n):
#     if isinstance(n, (int, float)):
#         return n * 5
#     return "provide valid integer"
#
# res = multiply_by_five(5.5)
# print(res)


#
# def func1():
#     print("entering func1")
#     func2()
#     print("exiting func1")
#
# def func2():
#     print("entering func2")
#     func3()
#     print("exiting func2")
#
# def func3():
#     print("entering func3")
#     print("exiting func3")
#
# func1()

# from math import pi
#
# # pi = "GLOBAL SPACE"
#
# def outer():
#     # pi = "ENCLOSED SPACE"
#     x = 10
#     def inner():
#         print(x)
#         # pi = "LOCAL SPACE"
#         print(pi)
#     return inner()
#
# outer()

# def hello():
#     return "from hello func"
#
# res = hello
# print(res)
# print(res())

# def outer():
#     # pi = "ENCLOSED SPACE"
#     x = 10
#     def inner():
#         print(x)
#         # pi = "LOCAL SPACE"
#         print(pi)
#     return inner()
#
# outer()

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# p = outer(10)
# print(p)
# q = p(5)
# print(q)
# res = outer(10)(20)
# print(res)

# def outermost():
#     def inner():
#         def innermost():
#             return "from inner most"
#         return innermost
#     return inner
#
# res = outermost()
# print(res)
# p = res()
# print(p)
# r = p()
# print(r)

'recursive'

# def fact(n):
#     if n <= 1:
#         return 1
#     return n * fact(n-1)
#
# res = fact(4)
# print(res)
# """
# fact(4)  -> return 4 * fact(3) ↑ return 4 * 6 = 24
# fact(3)  -> return 3 * fact(2) ↑ return 3 * 2 = 6
# fact(2)  -> return 2 * fact(1) ↑ return 2 * 1 = 2
# fact(1)  -> 1
# """

"decorator"


# def outer(func):
#     def wrapper():
#         print(f"before calling the {func.__name__} validations")
#         func()
#         print(f"after calling the {func.__name__} manipulations")
#     return wrapper
#
# @outer
# def hello():
#     print("from hello func")
#
# hello()
#
# @outer
# def another():
#     print("from another func")
#
# another()
#

'lambda'
"no name, one time usage, anonymous"

"""
lambda arguments : expression
arguments  : any number of arguments
expression : only one

by using lambda map filter reduce
"""
# add = lambda x, y: x + y
# print(add(5, 10))

'map'

# res = map(lambda x: x**2, range(5))
"[0, 1, 4, 9, 16]"
# res = map(lambda x: x.upper(), "python")
"['P', 'Y', 'T', 'H', 'O', 'N']"
# res = map(lambda x: x%2, range(5))
'[0, 1, 0, 1, 0]'
# res = map(lambda x: x%2==0, range(5))
"[True, False, True, False, True]"

# print(res)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(list(res))
# print(tuple(res))
# print(set(res))
# print(str(res))

'filter'

# res = filter(lambda x: x**2, range(5))
" 0  1  2  3   4"
"[0, 1, 4, 9, 16]"

# res = filter(lambda x: x.upper(), "python")
"  p    y    t    h     o   n"
"['P', 'Y', 'T', 'H', 'O', 'N']"
# res = filter(lambda x: x%2, range(5))
" 0  1  2  3  4"
'[0, 1, 0, 1, 0]'
# res = filter(lambda x: x%2==0, range(5))
"  0      1      2     3      4  "
"[True, False, True, False, True]"

# print(res)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(list(res))
# print(tuple(res))
# print(set(res))
# print(str(res))

'reduce'

# from functools import reduce
# ls = [10, 20, 30, 40, 50]
# res = reduce(lambda x, y: x+y, range(5))
"""
((((0+1)+2)+3)+4)
"""
# print(res)






