from typing import Any


class QueueNode:
    def __init__(self, priority: int, value: int):
        self.priority = priority
        self.value = value

    def __repr__(self):
        return f'{self.priority}-{self.value}'


class PriorityQueue:
    def __init__(self):
        self.queue: list[QueueNode] = []

    def sift_up(self, index: int) -> None:
        while index != 0 and self.queue[index].priority >= self.queue[index // 2].priority:
            self.queue[index], self.queue[index // 2] = self.queue[index // 2], self.queue[index]
            index //= 2

    def add(self, priority: int, value: int) -> None:
        self.queue.append(QueueNode(priority, value))
        self.sift_up(len(self.queue) - 1)

    def sift_down(self, index: int) -> None:
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        biggest_index = index
        if left_index < len(self.queue) and self.queue[left_index].priority > self.queue[biggest_index].priority:
            biggest_index = left_index
        if right_index < len(self.queue) and self.queue[right_index].priority > self.queue[biggest_index].priority:
            biggest_index = right_index
        if index != biggest_index:
            self.queue[index], self.queue[biggest_index] = self.queue[biggest_index], self.queue[index]
            self.sift_down(biggest_index)
        else:
            self.queue = self.queue[:-1]

    def extract(self) -> int:
        root = self.queue[0]
        self.queue[0] = self.queue[len(self.queue) - 1]
        self.sift_down(0)
        return root.value

    def remove(self, priority: int) -> None:
        index = 0
        while self.queue[index].priority != priority:
            index += 1
        if index >= len(self.queue):
            raise KeyError
        self.queue[index].priority = 10000000
        self.sift_up(index)
        self.extract()

    def __len__(self) -> int:
        '''метод, который возвращает длину списка'''
        return len(self.queue)

    def __str__(self):
        return f'{self.queue}'


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.add(1, 5)
    pq.add(5, 1)
    pq.add(2, 3)
    pq.add(7, 3)
    pq.add(4, 3)
    print(pq)
    pq.remove(7)
    print(pq)
    pq.remove(4)
    print(pq)
