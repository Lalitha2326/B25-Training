"""
Author : GOVIND
Date   : 09-12-2024
"""

def variable_args(*args, **kwargs):
    print("Positional arguments : ", args)
    print("Keyword arguments    : ", kwargs)
    print("Positional arguments type : ", type(args))
    print("Keyword arguments type   : ", type(kwargs))


variable_args(1, 2, 3, name='John', age=25)

# # req: the user can send any number of values, sum all those values
# # *args, **kwargs
# def add_fun(*args, **kwargs):
#     # count = 0
#     # for each in args:
#     #     count+=each
#     # return f"passed args are {args} and sum is {count}"
#     # return f"passed args are {args} and type is {type(args)}"
#     # return f"passed args are {kwargs} and type is {type(kwargs)}"
#     return f"passed positional args are {args} and keyword args are {kwargs}"


