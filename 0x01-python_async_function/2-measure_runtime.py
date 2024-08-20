#!/usr/bin/env python3

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    total_time = end - start
    return float(total_time / n)
