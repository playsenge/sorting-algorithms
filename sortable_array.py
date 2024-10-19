from collections.abc import Callable
from typing import Self
import random


class SortableArray:
    def __init__(self: Self, array: list[int], shuffle: bool):
        self.__array = array
        if shuffle:
            random.shuffle(self.__array)

    def __getitem__(self: Self, key: int | slice):
        return self.__array[key]

    def __setitem__(self: Self, key: int, value: int):
        self.__array[key] = value

    def __len__(self: Self):
        return len(self.__array)

    def __repr__(self: Self):
        return repr(self.__array)[0]

    def __iter__(self: Self):
        return iter(self.__array)

    def swap(self: Self, indexes: tuple[int, int]):
        self.__array[indexes[0]], self.__array[indexes[1]] = \
            self.__array[indexes[1]], self.__array[indexes[0]]
