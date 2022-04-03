from typing import Any


class QueueNode:
    def __init__(self, priority: int, value: int):
        self.priority = priority
        self.value = value

    def __repr__(self):
        pass
        # вывод узла


class PriorityQueue:
    def __init__(self):
        self.queue: list[QueueNode] = []

    def add(self, priority: int, value: int) -> None:
        pass
        # метод добавления узла в очередь (ключ - приоритет)

    def sift_up(self, index: int) -> None:
        pass
        # передаем индекс элемента, который нам нужно поднять вверх

    def extract(self) -> int:
        pass
        # удаление корня и его возвращение

    def sift_down(self, index: int) -> None:
        pass
        # опускает вниз элемент

    def __len__(self) -> int:
        '''метод, который возвращает длину списка'''
        return len(self.queue)

    def __repr__(self):
        pass
        # метод вывода массива
