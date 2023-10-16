import asyncio
from types import FunctionType


class AsyncLockedMethod:
    def __init__(self, func, lock):
        self.func = func
        self.lock = lock

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if asyncio.iscoroutinefunction(self.func):

            async def locked_method(*args, **kwargs):
                async with self.lock:
                    return await self.func(instance, *args, **kwargs)

        else:

            def locked_method(*args, **kwargs):
                return self.func(instance, *args, **kwargs)

        return locked_method


class AsyncSafeType(type):
    def __new__(cls, name, bases, dct):
        lock = asyncio.Lock()
        for attr_name, attr_value in dct.items():
            if isinstance(
                attr_value, (FunctionType, asyncio.coroutines.CoroWrapper)
            ) and not attr_name.startswith("__"):
                dct[attr_name] = AsyncLockedMethod(attr_value, lock)
        return super().__new__(cls, name, bases, dct)


class AsyncSafe:
    def __new__(cls, base_type):
        class Wrapped(base_type, metaclass=AsyncSafeType):
            pass

        return Wrapped

    @classmethod
    def __class_getitem__(cls, base_type):
        return cls(base_type)
