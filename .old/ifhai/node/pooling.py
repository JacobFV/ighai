from functools import reduce
import random
from typing import TypeVar


T = TypeVar("T")


def get_nth_entry(n):
    def _get_nth_entry(**kwargs) -> T:
        key = list(kwargs.keys())[n]
        return kwargs[key]

    return _get_nth_entry


get_first_entry = get_nth_entry(0)
get_last_entry = get_nth_entry(-1)


def get_random_entry(**kwargs) -> T:
    key = random.choice(list(kwargs.keys()))
    return kwargs[key]


def mean_pool(**kwargs) -> T:
    values = list(kwargs.values())
    return sum(values) / len(values)


def reduce_pool(fn):
    def _reduce_pool(**kwargs) -> T:
        values = list(kwargs.values())
        return reduce(fn, values)

    return _reduce_pool


sum_pool = reduce_pool(sum)
prod_pool = reduce_pool(lambda x, y: x * y)
