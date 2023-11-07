#!/usr/bin/env python3
"""Returns a list wating for an integer"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list wating for an integer"""
    delayed_tasks = [task_wait_random(max_delay) for count in range(n)]
    delay = await asyncio.gather(*delayed_tasks)
    return sorted(delay)
