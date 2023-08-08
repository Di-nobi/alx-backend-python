#!/usr/bin/env python3
'''ASYNC GENERATOR'''
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    '''Gets random float numbers in the range of 10'''
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(0.5)