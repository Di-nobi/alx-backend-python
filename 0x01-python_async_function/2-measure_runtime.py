#!/usr/bin/env python3
"""
Measures the total execution time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    roundup = time.perf_counter() - start_time
    return roundup
