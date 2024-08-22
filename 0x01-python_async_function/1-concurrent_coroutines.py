#!/usr/bin/env python3
"""This module implements an asynchronous coroutine"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """This async routine calls wait_n and spawns wait_random n
    times with the specified max_delay"""
    my_list = []
    for _ in range(n):
        my_list.append(await wait_random(max_delay))

    sorted_list = []
    for item in my_list:
        for i, value in enumerate(sorted_list):
            if item < value:
                sorted_list.insert(i, value)
                break
        else:
            sorted_list.append(item)

    return sorted_list
