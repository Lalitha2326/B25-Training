"""
Author : GOVIND
Date   : 21-11-2024
"""
"""
state:dt/ds,otuput,input

behaviour:bl crud operation DM, LOOPS,operaters
mutable:list,set,dict
immutable:int,float,complex,bl,str,tuple,None
iterable:str,list,tuple.set.dict,range
sequence;str,list,tuple,range
operaters:ac l ma ib
order:str,list,tuple,dic,range

DM:
---
                    T
if          i have more than 500 rupees   i will go to movie
--          --------------------           ------------------
constraint      situation/condition             decision

if elif else

1000 - shopping
5000 - trip

if condition1:
    execute this block of code if condition1 is True
elif condition2:
    execute this block of code if condition1 is false and condition2 should be true
elif condition3:
        execute this block of code if condition1, condition2 should be false and condition3 should be true
else:
    execute this block of code if above all conditions are false

and or not

T and T -> T
T or F  -> T
F or T  -> T 

"""
# money = int(input("enter money: "))

# if money >= 500:
#     print("go to movie")
#     print("helloo")
# else:
#     print("study python")
#
# # print("python")

# if money >= 500:
#     print("go to movie")
# elif money >= 1000:
#     print("go to shopping")
# elif money >= 5000:
#     print("go to trip")

# if money >= 5000:
#     print("go to trip")
# elif money >= 1000:
#     print("go to shopping")
# elif money >= 500:
#     print("go to movie")
# else:
#     print("study python")

# if money >= 5000:
#     print("go to trip")
# elif money >= 1000:
#     print("go to shopping")
# else:
#     print("go to movie")
#


# if money >= 5000:
#     print("go to trip")
# if money >= 1000:
#     print("go to shopping")
# if money >= 500:
#     print("go to movie")
# else:
#     print("study python")

# "name age location"
# dc = eval(input("enter user data: "))
# # dc1 = {"name": "ramesh"}
# # dc2 = {"name":"suresh", "age": 25}
# # dc = {"name": "rajesh", "age": 30, "location": "Bangalore"}
#
# data = {}
#
# if dc.get("name"):
#     data["name"] = dc.get("name")
# if dc.get("age"):
#     data["age"] = dc.get("age")
# if dc.get("location"):
#     data["location"] = dc.get("location")
#
# print(data)

# money = int(input("enter money: "))
# day_type = input("enter day_type weekday/weekend: ")
#
# #       T       and         T
# #       T       or         F
# if money >= 500 or day_type == 'weekend' :
#     print("go to movie")

"positive or negative or zero"

# num = int(input("enter a number: "))

# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# if num > 0:
#     print("positive")
#
# print("moving to next condition")
#
# if num < 0:
#     print("negative")
#
# print("moving to next condition")
#
# if num == 0:
#     print("zero")
#
# print("last condition")
#
#

"0 100 lessthan 35 fail greater than 35 just pass greaterthan 50 second class greater than 75 first class"

# marks = int(input("enter marks: "))

# if marks > 100 or marks < 0:
#     print("provide valid marks between 0-100")
# elif marks >= 75:
#     print("first class")
# elif marks >= 50:
#     print("second class")
# elif marks >= 35:
#     print("just pass")
# else:
#     print("fail")
#
# if marks > 100 or marks < 0:
#     print("provide valid marks between 0-100")
# elif 75 <= marks <= 100:
#     print("first class")
# elif 50 <= marks < 75:
#     print("second class")
# elif 35 <= marks < 50:
#     print("just pass")
# else:
#     print("fail")
#

day_type = input("enter day_type weekday/weekend: ")

if day_type == "weekday":
    print("go to office")
elif day_type == "weekend":
    activity_type = input("enter activity_type movie/party/trip: ")
    if activity_type == "movie":
        movie_type = input("enter movie_type ott/theatre: ")
        if movie_type == "ott":
            print("watch in ott")
        elif movie_type == "theatre":
            print("watch in theatre")
        else:
            print("enter valid movie_type ott/theatre: ")
    elif activity_type == "party":
        party_type = input("enter party_type house/outside: ")
        if party_type == "house":
            print("party in house")
        elif party_type == "outside":
            print("party outside")
        else:
            print("enter valid party type house/outside: ")
    elif activity_type == "trip":
        trip_type = input("enter trip_type local/outstation: ")
        if trip_type == "local":
            print("go to local trip")
        elif trip_type == "outstation":
            print("go to outstation trip")
        else:
            print("enter a valid trip type local/outstation")
    else:
        print("enter valid activity_type movie/party/trip: ")
else:
    print("provide valid day_type weekday/weekend")




