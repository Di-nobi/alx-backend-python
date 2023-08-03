#!/usr/bin/env python3
''' Task 11'''

from typing import Any, Mapping, Union, TypeVar

TypeVar = 'T'
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    '''Gets a value from a dictionary using a specific key'''
    if key in dct:
        return dct[key]
    else:
        return default