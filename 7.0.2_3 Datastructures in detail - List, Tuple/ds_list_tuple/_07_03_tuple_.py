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
max           - homogenous data(list, tuple)
min           - homogenous data(list, tuple)
len
in 

common builtin methods : count index


tuple:
-----
-> immutable
-> sequence
-> ordered
-> iterable
-> (), (ele,)
-> all dt/ds
-> homogenous data, heterogeneous data
-> 2


fetch builtin conversions - tuple(iterables)

"""
import sys

ls = [1, 2, 3, ["a", "b", "c"]]
tp = (1, 2, 3, ["a", "b", "c"])

print(sys.getsizeof(ls)) # 88
print(sys.getsizeof(tp)) # 72

# ls[3].append("new")
# print(ls)
ls.append("new")
tp[3].append("new")
print(tp)

print(sys.getsizeof(ls)) # 88
print(sys.getsizeof(tp)) # 72