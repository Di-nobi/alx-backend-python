#!/usr/bin/env python3
'''A function that takes a float as an argument and returns a function
multiplies a float by by multiplier'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''A function that takes a float as an argument and returns a function
    multiplies a float by by multiplier'''
    return lambda x: x * multiplier
