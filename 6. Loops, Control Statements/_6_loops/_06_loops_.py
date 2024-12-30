"""
Author : GOVIND
Date   : 22-11-2024
"""

"""
req:
----
state    : dt/ds input output
behavior :  BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict
immutable : int float complex bool None str tuple

iterable  : str list tuple set dict range
ordered   : str list tuple dict range

sequence  : str list tuple range

operators:
AC L MA IB

DM:
if elif else

loops
-----

for 

while

for each one who are present in this session       give 500 rupees
--                          ---                    ---------------
keyword                     membership operator         task


while
-----

condition based iteration
unknown iteration count

condition based iteration
--------------------------

initialize variable

while condition:
    task
    increment/decrement


unknown iteration count
-----------------------

while True:
    task
    condition
    break
    


"""
# s = "python"
# s = ["a", 1, "b", 2, "c"]
# s = ("a", 1, "b", 2, "c")
# s = {"a", 1, "b", 2, "c"}
# s = {"a": 10, "b": 20, "c":30}
# s = range(5, 10)
# for each in s:
#     print(each)
# print("hello")

# students = ["ramesh", "suresh", "harish", "rajesh", "rakesh", "sandesh"]

# for each in students:
#     print(each, end=', ')
# for each in students:
#     print("give 500 rupees to", each)
#
# print(each)
"""
each = "ramesh"
each = "suresh"
each = "harish"
each = "rajesh"
each = "rakesh"
each = "sandesh"



"""
# loop_num = 0
# for each in students:
#     # loop_num +=1
#     # print("give 500 rupees to", each) # task/action part
#     if each == "harish":
#         print("give 500 rupees to", each)  # task/action part
#         break
#     print("give 500 rupees to", each) # task/action part
#
# # print(loop_num)

# for each in students:
#     # print("give 500 rupees to", each) # task
#     if each == "harish":
#         # print("give 500 rupees to", each)  # task
#         continue
#     # print("give 500 rupees to", each) # task

# for each in students:
#     pass
#
# print("hello")

# for _ in range(10):
#     print("hello")


# num = int(input("enter a number: "))
#
# s = 1
#
# while num > 1:
#     # s = s * num
#     # num = num - 1
#     s *= num
#     num -= 1
#
# print(s)

"""
first loop  → num = 5 , s = 1  → 5 > 1 → s = 1 * 5 = 5  → num = 5 - 1 = 4
second loop → num = 4 , s = 5  → 4 > 1 → s = 5 * 4 = 20 → num = 4 - 1 = 3
third loop  → num = 3 , s = 20 → 3 > 1 → s = 20 * 3 = 60 → num = 3 - 1 = 2
fourth loop → num = 2 , s = 60 → 2 > 1 → s = 60 * 2 =120 → num = 2 - 1 = 1
fifth loop  → num = 1 , s = 120 → 1 > 1 - xxx 
"""

# secret = 3
#
# while True:
#     guess = int(input("enter number between 0- 9: "))
#     if guess == secret:
#         print("congratulations you have guessed the secret number")
#         break
#     else:
#         print("try again!")
# nums = [1, 2, 3, 4]
# fruits = ["apple", "banana", "orange", "mango", "grapes"]
# veggies = ["onion", "tomato", "chillies"]
#
# for num in nums:
#     print(num)
#     for fruit in fruits:
#         print("    ", fruit)
#         for veg in veggies:
#             print("        ", veg)

ls = [10 ,20, 30 ,40,50, 60, 70]

for each in ls:
    if each == 50:
        print("Yes")
        break
else:
    print("No")