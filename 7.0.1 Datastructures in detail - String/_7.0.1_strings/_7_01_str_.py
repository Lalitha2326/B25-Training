"""
Author : GOVIND
Date   : 25-11-2024
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
AC L MA IB

dm:
---
if elif else

loops:
------
for while

str:
----
-> immutable
-> sequence
-> ordered
-> iterable
-> '' "" """ """ ''' '''
-> 47


str list tuple - sequence ops
------------------------------
-> indexing - positive negative
-> slicing
-> concatenation  - with the same sequence type
-> repetition     - with only integers
-> min
-> max
-> len
-> in
-> common builtin methods - index count

-12-11 -10  -9  -8 -7   -6  -5 -4   -3  -2 -1                                           
p   y   t   h   o   n   .   w   o   r   l   d
0   1   2   3   4   5   6   7   8   9   10  11

 ... -5 -4 -3 -2 -1 0 1 2 3 4 5 6................
-20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8 -7   -6  -5 -4 -3  -2 -1 
-5 -4 -3 -2 -1 
-6  -5  -4  -3  -2 -1 

range(-(len(s), 0)                                         

1114111

fetch format / builtin conversions
"""
# s = "python"
# print(s, type(s))
# s = "python world"
# print(s[9])
# print(s[-4])
# print(s[0]) # first char/ele
# print(s[-1]) # last char/ele
# print(s[3: 9])
# print(s[-9: -3])
# print(s[9 : 4 : -1])
# print(s[-5: -11])

# n = s[-5: -11: -1]
# print(n, type(n))
# print(s[3:])
# print(s[-6:])
# print(s[:6])
# print(s[:-5])
# print(s[::])
# print(s[::2])
# print(s[::-1])
# print(s[2:15:3])
# print(s[16])
# print(s[3: -4])

# s1 = "python"
# s2 = "world"
# s2 = 5
# s3 = s1 + s2
# print(s3)

# s4 = s1 * s2
# print(s4)

# s = "PythonWorld"
# print(len(s))
# print("hon" in s)
# s = "▬☻╜¼ആ"
# print(min(s))
# print(max(s))
#
# print(ord("¼"))
# print(ord("☻"))
# print(chr(1114111))

"""
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[index])

-6  -5  -4  -3  -2 -1
p   y   t   h   o   n
0   1   2   3   4   5

0 1 2 3 4 5 = range(6) -> range(0, 6) -> start:0 stop:6 last_value = 5, num of ele = 6

len(s)

-6 -5 -4 -3 -2 -1 -> -(len(s)), 0

5 4 3 2 1 0 -> range(5, -1, -1)
20 -> 19

-1 -2 -3 -4 -5 -6 
-1 -2 -3...... -20
-1 -2 -3...... -12
-1 -2 -3 ..... -7
range(-1, -(len(s)+1), -1)
"""

# s = "python py"
"""
# forward
for each in s:
    print(each)

for each in range(len(s)):
    print(s[each])

for each in range(-(len(s)), 0):
    print(s[each])
"""

"""
# backward
for each in range(len(s)-1, -1, -1):
    print(s[each])

for each in range(-1, -(len(s)+1), -1):
    print(s[each])
"""

"format"

name = "ramesh"
age = 25
salary = 25639.36989

ls = ["suresh", 35, 26983.3245]
tp = ("paramesh", 30, 25000.3245)
dc = {"name": "Harish", "age": 45, "salary": 25698.36997}

# print("name is" + name + "age is" + str(age) + "salary is" + str(salary))

"f-strings"
# s = f"name is {name}, age is {age}, salary is {salary:.3f}"
# s = f"name is {ls[0]}, age is {ls[1]}, salary is {ls[2]:.3f}"
# s = f"name is {dc["name"]}, age is {dc["age"]}, salary is {dc["salary"]:.3f}"
# print(s)

".format"

# s = "name is {}, age is {}, salary is {:.2f}".format(name, age, salary)
# s = "name is {}, age is {}, salary is {:.2f}".format(*ls)
# s = "name is {}, age is {}, salary is {:.2f}".format(ls[0], ls[1], ls[2])
# s = "name is {name}, age is {age}, salary is {salary:.2f}".format(**dc)
# print(s)

'old style formatting - %s %d %f'
# s = "name is %s, age is %d, salary is %.2f"%(name, age, salary)
# s = "name is %s, age is %d, salary is %.2f"%(ls[0], ls[1], ls[2])
# s = "name is %s, age is %d, salary is %.2f"%tp
# s = "name is %(name)s, age is %(age)d, salary is %(salary).2f"%dc
# s = "name is %(name)s, age is %(age)s, salary is %(salary)s"%dc

# print(s)


# s = b"python"
# print(s, type(s))

# s = "it's very easy to learn python"
# s = '"python" is a programming language'
# s = """it's good to learn "python" """
# s = r"D:\tlass\B24 B25\7. Data structures in detail\7.0.1 Datastructures in detail - String\_7.0.1_strings"
# s = r"hi\ttabspace \nnewline \\ \'single quote\' \"double quote\""
# print(s)

# s = "python¼▬☻"
# print(s.encode())
# b = b'python\xc2\xbc\xe2\x96\xac\xe2\x98\xbb'
# print(b.decode())

"builtin meths"

# print(dir(str))
str_meths = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
             'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
             'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
             'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
             'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust',
             'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
             'swapcase', 'title', 'translate', 'upper', 'zfill']
# print(len(str_meths))

"""
lower upper capitalize title swapcase 
startswith endswith removeprefix removesuffix
format
find index
count
replace
split rsplit splitlines
strip rstrip lstrip
encode decode
zfill center
join

This is capitalize
This Is Title Case

   python.admin@email.com   
"""
# s = "PyThoN"
# print(s.lower())
# print(s)

# s = "pythonthon"
# print(s.index("t", 3, 10))
# print(s.find("l"))

# s = "python, is very, easy to, learn"
# print(s.split(',', maxsplit=2))
# print(s.split(',',  maxsplit=2))
# print(s.rsplit(",", maxsplit=2))
# s = """this is first line
# second line
# third line
# """
# print(s.splitlines(keepends=True))
# s = "¼"
# print(s.isnumeric())
# print(s.isdigit())

# s = "python"
# print(s.zfill(10))
# print(s.center(25, "*"))

# ls1 = ["python", "hello", "world"]
# firstname = "python"
# lastname = "flask"
# ls2 = [firstname, lastname]
# print(".".join(ls2)+"@ferilionlabs.com")
# print(".".join(ls1))

# "conversions - str()"
# s = 10
# print(str(s))
"""
s = "python"
print(s[0])
s[0] = "b"
"""
# s = "python"
# print(s[0])
# s[0] = "b"