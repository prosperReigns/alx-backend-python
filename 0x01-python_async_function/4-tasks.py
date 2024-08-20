#!/usr/bin/env python3

import asyncio
from typing import callable
def task_wait_n(callable):
    return asyncio.create_task(task_wait_random())
