#!/usr/bin/env python3
'''A function that takes a string
and an int and return a tuple'''


from typing import Union, Tuple
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A function that takes a string
and an int and return a tuple'''
    return (k, v**2)
