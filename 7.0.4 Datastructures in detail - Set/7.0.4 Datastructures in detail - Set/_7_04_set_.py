"""
Author : GOVIND 
Date   : 27-11-2024
"""
"""
req:
----
state    : dt/ds input output
behavior : BL - CRUD - DM LOOPS OPERATORS

mutable   : list set dict
immutable : int float complex bool None str tuple

iterables : str list tuple set dict range
ordered   : str list tuple dict range
sequence  : str list tuple range

OPERATORS:
----------
AC L MA IB

DM
--
if elif else

LOOPS
-----
for while -> break continue pass

sequence ops:
--------------
indexing - positive negative
slicing 
concatenation  - with same sequence type
repetition     - with only int
min            - list tuple (homogenous data) 
max            - list tuple (homogenous data) 
len
in
count index

set:
----
-> mutable
-> unordered
-> iterable
-> set elements unique
-> set elements immutable
-> set() set({})
-> 17

comprehension and conversion
"""

# st = {1, 2.5, 4+5j, None, False, "python", (3, 4)}
# print(st, type(st))

# st = {1, 1, 1, 1, 1, 2, 3, 2, 3}
# s = 3 + 5
# print(s)
# st = {"python", "hello", "world"}
# print(st)
# print(min(st))
# print(max(st))
# print(len(st))
# print("hello" in st)

# st = {"a", 1, "c", 5, "d", 2, "e", 3}
#
# for each in st:
#     print(each)


# st = set()
# print(st, type(st))

# print(dir(set))

st_meths = ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
            'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
            'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

"""
add    : add
remove : clear pop remove discard

union               intersection              difference                symmetric_difference   
update              intersection_update       difference_update         symmetric_difference_update

isdisjoint issubset issuperset
copy
"""


# st1 = {1, 2, 3, 4}
# st2 = {3, 4, 5, 6}
# st2 = [3, 4, 5, 6]
# st2 = (3, 4, 5, 6)
# st2 = "python"
# st2 = {"a": 10, "b": 20, "c": 30}
# st1.add((1,2,3))
# print(st1)

# st1.clear()
# x = st1.pop()
# print(x)
# st1.remove(6)
# st1.discard(6)
# print(st1)

# st3 = st1.union(st2)
# print(st3)
# st1.update(st2)
# print(st1)
# print(st2)

# st3 = st1.intersection(st2)
# print(st3)
# st1.intersection_update(st2)
# print(st1)
""
# st3 = st1.difference(st2)
# print(st3)
# st3 = st1 - st2
# print(st3)

# st1.difference_update(st2)
# print(st1)
""
# st3 = st1.symmetric_difference(st2)
# print(st3)
# st1.symmetric_difference_update(st2)
# print(st1)
""
# st1 = {3, 4, 5, 6, 7, 8}
# st2 = {1, 2}
# print(st1.isdisjoint(st2))

"set comprehension"
"st = {expression for item in iterable if condition(optional)}"
# st = {x**2 for x in range(5)}
# print(st)

"conversions - set(iterables)"
"note: in iterables it should contain only immutable dt/ds"
# ls = [1, 2, 3]
# st = set(ls)
# print(st)

"""
st = {"a", 1, "b"}

st = set()
st.add()

st = {expression for item in iterable if condition(optional)}

st = set(iterables)

"""

ls = [1, 2, 3, 4, 5]

ls2 = [x for x in ls if x%2==0]

# for each in ls:
#     if each%2==0:
#         ls2.append(each)
print(ls2)


