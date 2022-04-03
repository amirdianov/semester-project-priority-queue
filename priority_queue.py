from typing import Any


class QueueNode:
    def __init__(self, priority: int, value: int):
        self.priority = priority
        self.value = value

    def __repr__(self):
        return f'({self.priority},{self.value})'


class PriorityQueue:
    def __init__(self):
        self.list: list[QueueNode] = []

    def add(self, priority: int, value: int) -> None:
        self.list.append(QueueNode(priority, value))
        self.sift_up(len(self) - 1)

    def sift_up(self, idx: int) -> None:
        """sifts up element of Heap and put it into correct place"""
        while idx > 0 and self.list[idx].priority > self.list[(idx - 1) // 2].priority:
            self.list[idx], self.list[(idx - 1) // 2] = self.list[(idx - 1) // 2], self.list[idx]
            idx = (idx - 1) // 2

    def extract(self) -> int:
        """deletes root from Heap and returns it"""
        if len(self) == 1:
            return self.list.pop().value
        head: QueueNode = self.list[0]
        self.list[0] = self.list.pop()
        self.sift_down(0)
        return head.value

    def sift_down(self, idx: int) -> None:
        """sifts down element of Heap and put it into correct place"""
        while 2 * idx + 1 < len(self.list):
            max_priority: int = self.list[2 * idx + 1].priority
            max_idx: int = 2 * idx + 1
            if 2 * idx + 2 < len(self.list) and self.list[2 * idx + 2].priority > max_priority:
                max_priority = self.list[2 * idx + 2].priority
                max_idx: int = 2 * idx + 2
            if max_priority <= self.list[idx].priority:
                break
            self.list[idx], self.list[max_idx] = self.list[max_idx], self.list[idx]
            idx = max_idx
        # опускает вниз элемент

    def __len__(self) -> int:
        '''метод, который возвращает длину списка'''
        return len(self.list)

    def __repr__(self) -> str:
        return repr(self.list)


