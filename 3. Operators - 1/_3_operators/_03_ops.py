"""
Author : GOVIND
Date   : 18-11-2024
"""
"""
req:
----
state    : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict - CRUD
immutable : int float complex bool None str tuple - CRD

iterables : str list tuple set dict
sequence  : str list tuple

operators:
----------
symbols keywords

AC L MA IB

""



"""

"""
"add two int provide the result"
"X + Y print"
"identify major minor"

age = 20 -> major
age = 6  -> minor
   
if the age is greater than or equal to 18 print major else print minor

age = int(input("enter age: "))

if age >= 18:
    print("major")
else:
    print("minor")
"""

"Airthemtic "
"+ - * / // % **"

# n1 = 5+6j
# n2 = 2

# print(n1 ** n2)
# print(n1 / n2)
# print(n1 // n2)
# print(n1 % n2)

"Comparison"
"== != > < >= <="

# n1 = {40:30}
# n2 = {50:60}
#
# # print(ord("a"))
# # print(ord("A"))
# print(n1 > n2)

"logical - and or not  - DM"

"""
p       q       p and q         p or q
-       -       -------         -------
T       T           T               T
T       F           F               T
F       T           F               T
F       F           F               F

not

10 users 1 2 3 4 5 6 7 8 9 10
1 -> data
11 -> None
"""
# print(True and False)
# print(5 and 10)
# print(10 and 5)
# print(10 and "a")
# print("a" and 5)
# print("a" and "b")
# print(1 and 0)
# print(0 and 1)
# print(5 and 0)
# print(0 and 5)
# print("" and "a")
# print([] and "")

# print(True or False)
# print(5 or 10)
# print(10 or 5)
# print(10 or "a")
# print("a" or 5)
# print("a" or "b")
# print(1 or 0)
# print(0 or 1)
# print(5 or 0)
# print(0 or 5)
# print("" or "a")
# print([] or "")
# print("hello")

# x = 10
# x = 0
# x = []
# x = ""
# x = {}
# x = set()
# x = None
#
# if not x:
#     print("data is not present")
# else:
#     print("data is present")