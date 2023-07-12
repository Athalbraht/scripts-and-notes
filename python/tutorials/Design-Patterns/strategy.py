import random
from abc import ABC, abstractmethod


class Element():
    def __init__(self, id):
        self.id = id


class OrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, _list: list[Element]) -> list[Element]:
        pass


class Dec(OrderingStrategy):
    def create_ordering(self, _list: list[Element]) -> list[Element]:
        return sorted(_list, reversed=True)


class Inc(OrderingStrategy):
    def create_ordering(self, _list: list[Element]) -> list[Element]:
        return sorted(_list)


a: list = [12, 3, 5, 3, 3, 45, 5, 6, 4, 23, 2]

sorter : OrderingStrategy = Dec()
sorter : OrderingStrategy = Inc()
