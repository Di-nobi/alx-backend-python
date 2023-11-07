#!/usr/bin/env python3

'''A program that takes in an integers and wait for its delay time'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Awaits for a random digit'''
    LetsWait = max_delay * random.random()
    await asyncio.sleep(LetsWait)
    return LetsWait
