from functools import reduce
import random
from abc import ABC, abstractmethod
import asyncio
import threading
from typing import Callable, Generic, TypeVar, Any


from ifhai.utils.parellelization.multithreading_safety import ThreadSafe
from ifhai.models.pooling import get_first_entry

T = TypeVar("T")


class Port(Generic[T]):
    pool_op: Callable[[dict[str, T]], T] = get_first_entry

    pool: ThreadSafe[dict]

    pool_queue: asyncio.Queue[ThreadSafe[dict]] = asyncio.Queue()

    def input(self, key, value):
        self.pool[key] = value
