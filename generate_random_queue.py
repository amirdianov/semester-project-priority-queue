'''
generation dataset
'''
# Здесь будет производиться генерация наборов данных и их запись в файл .txt
import random
from priority_queue import PriorityQueue, QueueNode

COUNT = 1
path = fr'\{COUNT}'


def random_queue() -> PriorityQueue:
    '''создание рандомной очереди'''
    testing_queue = PriorityQueue()
    global COUNT
    for i in range(10000):
        perem = (random.randint(-10000, 10000), random.randint(-10000, 10000))
        testing_queue.add(perem[0], perem[1])

    with open(path, 'a', encoding='utf-8') as file:
        for node in testing_queue.queue:
            priority, value = node.priority, node.value
            file.write(f'{priority}: {value}')
    COUNT += 1
    return testing_queue
