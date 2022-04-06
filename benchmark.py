import random

from typing import Callable
from priority_queue import PriorityQueue
from generate_random_queue import random_queue
from time import time

def time_it(function: Callable) -> Callable:
    def wrap_and_time(*args):
        start = time()
        function(*args)
        end = time()
        result = end - start
        return result

    return wrap_and_time

def start_testing(idx: int, name_method: str, tests_count: int):
    new_queue = random_queue(idx, name_method, tests_count)
    return new_queue

@time_it
def check_add(test_queue: PriorityQueue):
    queue: PriorityQueue = PriorityQueue()
    for node in test_queue.queue:
        queue.add(node.priority, node.value)

@time_it
def check_extract(test_queue: PriorityQueue):
    while len(test_queue):
        test_queue.extract()

for i in range(1, 6):
    test_add_queue: PriorityQueue = start_testing(i, 'add', 10 ** i)
    print(check_add(test_add_queue))
print('-' * 10)
for i in range(1, 6):
    test_extract_queue: PriorityQueue = start_testing(i, 'extract', 10 ** i)
    print(check_extract(test_extract_queue))
#COUNT = 1
#start_testing()
#start_testing()
