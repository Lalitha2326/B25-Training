"""
Author : GOVIND
Date   : 20-11-2024
"""
"""
req:
----
state   : dt/ds input output
behavior: BL - CRUD - DM LOOPS OPERATORS


mutable   : list set dict  - CRUD
immutable : int float complex bool None str tuple - CRD

iterables  : str list tuple set dict range
sequence   : str list tuple

OPERATORS
AC L MA IB

==(values) is(memory address)

int   .......-3 -2 -1 0 1 2 3 .........  immutable
float decimals salary  3.5              immutable
complex  3+5j                           immutable

Bool  True(1) False(0)                  immutable
None NA nothing                         immutable

str - 
immutable
ordered
sequence
'a' "abc" """ """ ''' '''
47 builtin methods - count index

list
------
mutable
ordered
sequence
[]
all dt/ds
homogenous data,  heterogeneous data
builtin methods - 11 - count index

tuple
-----
immutable
ordered
sequence
()
all dt/ds
homogenous data,  heterogeneous data
builtin methods - 2 count index

set :
-----
mutable
unordered
unique elements
immutable
set()
{}
builtin methods - 17

mapping type - dict
-------------------
mutable
ordered
{}
key: value pairs
keys - unique, immutable
values - any dt/ds
11 - builtin methods
"""
# s = """first line
# second line
# third line
# fourth line"""
# print(s)
#
# s = "python"
# z = s.upper()
# print(z)
# print(s)

# ls = {1, 2.5, 3+5j, True, None, "str", (30, 40)}
# print(ls, type(ls))

# emp_data = [10, "ramesh", "bangalore", "chennai", 25000, 5000, True, False]
# emp_id = [10, 11, 12, 13]
# emp_names = ["ramesh", "suresh", "rajesh"]
# emp_salary = [1000, 2000, 1000, 5000]
# emp_dc = {
#           "id": 10,
#           "name": "ramesh",
#           "curr_loc": "bangalore",
#           "work_loc": "chennai",
#           "salary": 25000,
#           "incentive": 5000,
#           "is_perm": True,
#           "wfh": False
#           }

"""
range - range is a function which is going to generate sequence of numbers

loops

range(n)   -> range(0, n) -> start: 0, stop: n, step: 1, last_value: n-1, total: stop - start
range(m, n)               -> start: m, stop: n, step: 1, last_value: n-1, total: stop - start
range(p, q, r)            -> start: p, stop: q, step: r
"""

# rg = range(5, 15, 2)
# print(rg)
# 10 - 5 / 3 = 1.ss -> 2 f - 1

# for each in range(5, 10, 3):
#     print(each)
"""
...........-9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9..........

"""
for each in range(-5, -10, -2):
    print(each)










