#!/usr/bin/env python3
'''Last Task'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''Async_comprehension to be executed 4 times'''
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    return time.time() - start