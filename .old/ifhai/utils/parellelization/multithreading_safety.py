from types import FunctionType
import threading


class LockedMethod:
    def __init__(self, func, lock):
        self.func = func
        self.lock = lock

    def __get__(self, instance, owner):
        if instance is None:
            return self

        def locked_method(*args, **kwargs):
            with self.lock:
                return self.func(instance, *args, **kwargs)

        return locked_method


class ThreadSafeType(type):
    def __new__(cls, name, bases, dct):
        lock = threading.Lock()
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, FunctionType) and not attr_name.startswith("__"):
                dct[attr_name] = LockedMethod(attr_value, lock)
        return super().__new__(cls, name, bases, dct)


class ThreadSafe:
    def __new__(cls, base_type):
        class Wrapped(base_type, metaclass=ThreadSafeType):
            pass

        return Wrapped

    @classmethod
    def __class_getitem__(cls, base_type):
        return cls(base_type)
