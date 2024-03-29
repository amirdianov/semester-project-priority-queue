'''
PriorityQueue
'''
from time import time

import graphics


class QueueNode:
    '''QueueNode class'''

    def __init__(self, priority: int, value: int):
        self.priority = priority
        self.value = value

    def something(self):
        '''something more'''

    def __repr__(self):
        return f'{self.priority}: {self.value};\n'


class PriorityQueue:
    '''PriorityQueue class'''

    def __init__(self):
        self.queue: list = []

    def add(self, priority: int, value: int) -> None:
        '''метод добавления узла в очередь (ключ - приоритет)'''
        node = QueueNode(priority, value)
        self.queue.append(node)
        self.sift_up(len(self) - 1)

    def sift_up(self, index: int) -> None:
        '''передаем индекс элемента, который нам нужно поднять вверх'''
        parent_ind = (index - 1) // 2
        while index != 0 and self.queue[index].priority >= self.queue[parent_ind].priority:
            self.queue[index], self.queue[parent_ind] = self.queue[parent_ind], self.queue[index]
            index = parent_ind
            parent_ind = (index - 1) // 2

    def extract(self) -> int:
        '''удаление корня и его возвращение'''
        root = self.queue[0]
        if len(self) == 1:
            return self.queue.pop()
        self.queue[0] = self.queue.pop()
        self.sift_down(0)
        return root.value

    def sift_down(self, index: int) -> None:
        '''опускает вниз элемент'''
        while 2 * index + 1 < len(self):
            maxim_node = self.queue[2 * index + 1]
            maxim_index = 2 * index + 1
            if 2 * index + 2 < len(self) and \
                    maxim_node.priority < self.queue[2 * index + 2].priority:
                maxim_node = self.queue[2 * index + 2]
                maxim_index = 2 * index + 2
            if maxim_node.priority <= self.queue[index].priority:
                return
            self.queue[maxim_index], self.queue[index] = \
                self.queue[index], self.queue[maxim_index]
            index = maxim_index

    def __len__(self) -> int:
        '''метод, который возвращает длину списка'''
        return len(self.queue)

    def __repr__(self):
        '''метод вывода списка'''
        ans = ''
        for i in self.queue:
            ans += i.__repr__()
        return ans

    def get_root(self):
        return self.queue[0]

    def search(self, priority):
        for node in self.queue:
            if node.priority == priority:
                return node.value
        raise KeyError


# queue = PriorityQueue()
# x = PriorityQueue()
# x.add(1, 1)
# x.add(2, 2)
# x.add(3, 3)
# x.add(4, 4)
# x.add(5, 5)
# mas = []
# start = time()
# x.extract()
# mas.append(time() - start)
# start = time()
# x.extract()
# mas.append(time() - start)
# start = time()
# x.extract()
# mas.append(time() - start)
# start = time()
# x.extract()
# mas.append(time() - start)
# start = time()
# x.extract()
# mas.append(time() - start)
#
# graphics.paint_grafics(mas, [5, 4, 3, 2, 1])
