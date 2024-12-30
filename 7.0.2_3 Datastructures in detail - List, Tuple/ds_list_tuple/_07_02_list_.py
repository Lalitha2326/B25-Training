"""
Author : GOVIND
Date   : 26-11-2024
"""
"""
req:
----
state    : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict
immutable : int float complex bool None str tuple

iterables  : str list tuple set dict range
sequence   : str list tuple range

ordered    : str list tuple dict range

operators:
----------
AC L MA IB    == vs is

dm:
---
if elif else

loops:
------
for while  - break continue pass


sequence ops:
-------------
indexing  - positive negative
slicing
concatenation - with same sequence type
repetition    - only with int
max
min
len
in 

common builtin methods : count index


list:
-----
-> mutable
-> sequence
-> ordered
-> iterable
-> []
-> all dt/ds
-> homogenous data, heterogeneous data
-> 11


fetch builtin comprehension conversions


ls[0]
ls[1]
ls[2]
ls[3]
ls[4]

99 ...... 0
4 3 2 1 0 = len(ls) = 5
9 8 7 6 5 4 3 2 1 0 - len(ls) = 10

-4 -3 -2 -1 0 1 2 3

range(len(ls)-1, -1, -1)


-1 -2 -3 ............ -10
-1 -2 -3 -4 -5
-1 -2 -3 -4 -5 -6 -7 -8

range(-1, -(len(s)+1), -1)
"""
#    -10  -9   -8    -7     -6      -5      -4      -3      -2          -1
# ls = [1, 2.3, 4+5j, True, None, "python", [2, 4], (6, 8), {7, 9}, {"a":10, "b":20}]
#     0   1     2      3    4       5       6       7       8           9
# print(ls, type(ls))

# print(ls[0])
# print(ls[-1])
# print(ls[3: 7])
# print(ls[-8:-5])
# print(ls[2:9:2])
# print(ls[3:])
# print(ls[:-5])
# print(ls[::])
# print(ls[::-1])
# print(ls[2:-2])
# print(ls[7:2:-1])
# print(ls[-2: -8: -1])
# ls2 = ["new", "a", "b"]

# ls3 = ls + ls2
# print(ls3)
# ls4 = ls2 * False
# print(ls4)

# ls = ["python", "pello", "porld"]
# ls = [[2, 100], [100, 2], [50, 250]]
# ls = [{4, 6}, {50, 250}, {2, 100}]
# ls = [{"a": 10}, {"b": 2}, {"c": 500}] - xx
# print(max(ls))
# print(min(ls))

# ls = [2.3, 4+5j, True, None, "python", [2, 4], (6, 8), {7, 9}, {"a":10, "b":20}]
#                                                                   "pyth"
# print(len(ls))
# print(1 in ls)

'fetch'
#    -10  -9   -8    -7     -6      -5      -4      -3      -2          -1
# ls = [1, 2.3, 4+5j, True, None, "python", [2, 4], (6, 8), {7, 9}, {"a":10, "b":20}]
'#     0   1     2      3    4       5       6       7       8           9'
"""
for each in ls:
    print(each)

for each in range(len(ls)):
    print(ls[each])

for each in range(-(len(ls)), 0):
    print(ls[each])
"""
"""
for each in range(len(ls)-1, -1, -1):
    print(ls[each])

for each in range(-1, -(len(ls) +1 ), -1):
    print(ls[each])
"""

"builtin - 11"
# print(dir(list))

ls_meth = ['append', 'clear', 'copy', 'count', 'extend', 'index',
           'insert', 'pop', 'remove', 'reverse', 'sort']

"""
count, index

add    : append insert extend
remove : pop remove clear

reverse sort copy

"""
# ls = ["a", "b"]
# print(ls.count("c"))

# ls = ["a", "b", "c", "d"]
#      0    1    2    3
# print(id(ls))
# ls.append("new")
# ls.append([10,20,30])
# ls.append({"a":10, "b":20})
# print(ls)
# print(id(ls))
# ls.insert(100, "python")
# print(ls)
# print(ls[4])
# ls.extend("python")
# ls.extend([10, 20, 30, 40])
# ls.extend({10, 20, 30, 40})
# ls.extend({"a": 10, "b": 20, "c": 30})
# ls.extend(range(10, 20))
# print(ls)

# ls2 = []
# # ls.append()
# for each in range(10):
#     if each%2 == 0:
#         ls2.append(each)
# print(ls2)
# ls.clear()
# print(ls)

# x = ls.pop()
# print(x)
# x = ls.pop(2)
# print(x)
# print(ls)

# ls.remove("f")
# print(ls)

# ls = [10, 5, 6, 2, -1, 50, 26]
# ls.sort()
# print(ls)
# n = sorted(ls)
# print(n)
# print(ls)

'[-1, 2, 5, 6, 10, 26, 50]'

'comprehension - [expression for item in iterable if condition(optional)]'
"""
ls = [1, 2, 3, 4]

ls = []
ls.append()

ls = [expression for item in iterable if condition(optional)]

ls = list(iterables)

"""
# ls = [x**2 for x in range(5, 15) if x%2==0]
# print(ls)
# s = "python"
# ls = [x.upper() for x in s]
# print(ls)

'conversions - list(iterables)'
#
# ls = list("python")
# print(ls)

'item assignment'
ls = ["a", 1, "b", 2, "c", "d"]
# print(ls[2])
ls[2] = "new"
print(ls)





