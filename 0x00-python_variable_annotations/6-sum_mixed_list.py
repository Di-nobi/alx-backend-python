#!/usr/bin/env python3
'''A function that takes a list of integers and floats
and returns the sum as a float'''

from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''A function that takes a list of integers and floats
    and returns the sum as a float'''
    return float(sum(mxd_lst))