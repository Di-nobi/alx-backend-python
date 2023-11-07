#!/usr/bin/env python3
"""
Executing coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Gets the lists of the delays (floats value)"""
    mergelist = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(mergelist)
