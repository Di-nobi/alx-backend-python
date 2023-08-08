#!/usr/bin/env python3
'''ASYNC COMPREHENSIONS'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using an async comprehensing over async_generator'''
    num = []
    async for i in async_generator():
        num.append(i)
    return num