'''
generation dataset
'''
# Здесь будет производиться генерация наборов данных и их запись в файл .txt
import random
from priority_queue import PriorityQueue


def random_queue(count) -> PriorityQueue:
    '''создание рандомной очереди'''
    path = fr'C:\Users\amird\PycharmProjects\
    semester-project-priority-queue\dataset_local\{count}.txt'
    testing_queue = PriorityQueue()
    for _ in range(10):
        perem = (random.randint(-10000, 10000), random.randint(-10000, 10000))
        testing_queue.add(perem[0], perem[1])

    with open(path, 'a', encoding='utf-8') as file:
        for node in testing_queue.queue:
            priority, value = node.priority, node.value
            file.write(f'{priority}: {value}\n')
    count += 1
    return testing_queue
