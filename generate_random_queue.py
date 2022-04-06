'''
generation dataset
'''
# Здесь будет производиться генерация наборов данных и их запись в файл .txt
import random
from priority_queue import PriorityQueue

PATH: str = 'C:/Users/amird/PycharmProjects/semester-project-priority-queue/dataset_local/'


def random_queue(count, name_method, tests_count: int) -> PriorityQueue:
    '''создание рандомной очереди'''
    path = PATH + fr'{name_method}/' \
                  fr'{count}.txt'
    testing_queue = PriorityQueue()
    for _ in range(tests_count):
        perem = (random.randint(-10000, 10000), random.randint(-10000, 10000))
        testing_queue.add(perem[0], perem[1])

    with open(path, 'w', encoding='utf-8') as file:
        for node in testing_queue.queue:
            priority, value = node.priority, node.value
            file.write(f'{priority}: {value}\n')
    count += 1
    return testing_queue
