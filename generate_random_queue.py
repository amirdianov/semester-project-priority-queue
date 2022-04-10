'''
generation dataset
'''
# Здесь будет производиться генерация наборов данных и их запись в файл .txt
import random
from priority_queue import PriorityQueue

PATH: str = '/Users/bulat/PycharmProjects/semester-project-priority-queue/dataset_local/'


def random_queue(queue_length: int, name_method: str) -> PriorityQueue:
    '''создание рандомной очереди'''
    path = PATH + fr'{name_method}/' \
                  fr'{queue_length}.txt'
    testing_queue = PriorityQueue()
    for _ in range(queue_length):
        random_priority, random_value = random.randint(-10000, 10000), random.randint(-10000, 10000)
        testing_queue.add(random_priority, random_value)

    with open(path, 'w', encoding='utf-8') as file:
        for node in testing_queue.queue:
            priority, value = node.priority, node.value
            file.write(f'{priority}: {value}\n')
    return testing_queue
