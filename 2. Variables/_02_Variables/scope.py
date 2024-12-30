"""
Author : GOVIND
Date   : 15-11-2024
"""
# LEGB RULE example
# Local Enclosed Global Builtin

from math import pi
pi = 'global pi variable'


def outer():
    pi = 'enclosed space variable'
    def inner():
        pi = 'local space variable'
        print(pi)
    inner()


outer()
