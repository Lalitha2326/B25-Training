"""
Author : GOVIND
Date   : 28-11-2024
"""
"""
req:
----
state   : dt/ds input output
behavior: BL - CRUD - DM LOOPS OPERATORS


mutable   : list set dict
immutable : int float complex bool None str tuple

iterables : str list tuple set dict range
ordered   : str list tuple dict range
sequence  : str list tuple range

operators:
----------
AC L MA IB

dm:
---
if elif else

loops:
------
for while  -> break continue pass

sequence ops:
-------------
indexing  - positive negative
slicing  
concatenation  - with the same sequence type
repetition     - only with integers
min            - list tuple homogenous data
max            - list tuple homogenous data
len
in
common builtin methods : count index

list -> append insert extend pop remove clear count index reverse sort copy
set  -> add pop remove clear discard union update intersection intersection_update difference difference_update
        symmetric_difference symmetric_difference_update isdisjoint issubset issuperset copy
        
dict:
-----
-> mutable
-> mapping type
-> ordered (3.7+)
-> {}
-> key: value pairs
-> keys   -> unique immutable
-> values -> any dt/ds
-> 11

-> values - int float bool str list dict
-> keys   - str



"""
# dc = {"name": "ramesh", "age": 25, "sal": 2365.36, "is_perm": True, "Phn_numbrs": [98566941, 9231147]}
# print(dc, type(dc))
# print(min(dc))
# print(max(dc))
# print(len(dc))
# print(25 in dc)
# dc = {}

# print(dir(dict))
dc_meths = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
            'popitem', 'setdefault', 'update', 'values']

"""
add  : update
removing : pop popitem clear 

fetch : keys values items

setdefault
fromkeys
get
copy

[('name', 'ramesh'), ('age', 25), ('sal', 2365.36), ('is_perm', True), ('phn_numbers', [98566941, 9231147])]4

s = "python"
s[0] = "b"
print(s)

ls =[1 , 2, 3]
ls[0] = 4
[4,2,3]

"""

# dc = {"name": "ramesh", "age": 25, "sal": 2365.36, "is_perm": True, "phn_numbers": [98566941, 9231147]}
# print(dc)
# print(len(dc))
'update'
# dc2 = {"a":10, "b": 20}
# dc2 = [10, 20, 30]
# dc2 = [("A", 10), {"B", 20}, ["C", 30]]
# dc.update(dc2)
# print(dc)

'pop popitem clear'
# dc = {"name": "ramesh", "age": 25, "sal": 2365.36, "is_perm": True, "phn_numbers": [98566941, 9231147]}
# x = dc.pop("loc", "Bangalore")
# print(x)
# print(dc)
# x = dc.popitem()
# print(x)
# print(dc)

'fetch'
# dc = {"name": "ramesh", "age": 25, "sal": 2365.36, "is_perm": True, "phn_numbers": [98566941, 9231147]}

# for each in dc:
#     print(each)
'keys values items'

# ks = dc.keys()
# print(ks, type(ks))

# for each in dc.keys():
#     print(each)

# vals = dc.values()
# print(vals, type(vals))

# for each in dc.values():
#     print(each)

# ls = [('name', 'ramesh', "a"), ('age', 25,"b"), ('sal', 2365.36, "c"), ('is_perm', True,"d"), ('phn_numbers', [98566941, 9231147], "e")]

# each = ("name", "ramesh")
# a, b = ('name', 'ramesh')
#
# x , y , z = "pyt"
#
# print(a)
# # print(b)

# for k, v, p in ls:
#     print(k)
#     print(v)
#     print(p)
#

# itms = dc.items()
# print(itms, type(itms))

# for each in dc.items():
#     print(each)

# for key, value in dc.items():
#     print(f"key is {key}")
#     print(f"value is {value} \n")

'setdefault'
# dc = {"name": "ramesh", "age": 25, "sal": 2365.36, "is_perm": True, "phn_numbers": [98566941, 9231147]}
# dc.setdefault("location", "bangalore")
# print(dc)

'fromkeys'
# ks = {}
# an = {"hh": 10, "bb": 20}
# # dc = dict.fromkeys("python", 100)
# dc = an.fromkeys([10, 20, ("a", "b")], 100)
# print(dc)
# print(ks)

# dc = {"name": "ramesh", "age": 25, "sal": 2365.36, "is_perm": True, "phn_numbers": [98566941, 9231147]}

# x = dc.get("loc", "bangalore")
# x = dc['loc']
# print(x)
# print(dc)

# dc = {"name": "ramesh", "age": 25, "sal": 2365.36, "is_perm": True, "phn_numbers": [98566941, 9231147]}
# # dc["location"] = "banaglore"
# dc['name'] = "suresh"
# print(dc)

# dc = {}
# dc["name"]= "ramesh"
# dc["age"] = 25
# print(dc)

"comprehensions - "
"dc = {key expression: value expression for item in iterables if condition optional}"

# dc = {x:x**2 for x in range(6)}
# print(dc)

# ls1 = ["a", "b", "c", "d"]
# ls2 = [10, 20, 30]
#
# dc = {k:v for k,v in zip(ls1, ls2)}
# print(dc)

"conversions - dict()"

# ls = [('name', 'ramesh'), {'age', 25}, ['sal', 2365.36], ('is_perm', True), ('phn_numbers', [98566941, 9231147])]
# dc = dict(ls)
# print(dc)
# ls1 = ["a", "b", "c", "d"]
# ls2 = [10, 20, 30]
# dc = dict(zip(ls1, ls2))
# print(dc)

"collections - counter"
import collections

"""
update setdefault
pop popitem clear
keys values items
fromkeys
get
dc[]
copy

"""
# dc = {"a": 10}
#
# if dc.get("a"):
#     print("data is present")
# else:
#     print("no data")












