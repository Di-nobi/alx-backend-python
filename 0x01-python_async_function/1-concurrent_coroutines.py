#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random

from typing import List
import random
import asyncio

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Executing multiple coroutines at the same time with async'''
    mergelist = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(mergelist)