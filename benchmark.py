import random

from typing import Callable
from priority_queue import PriorityQueue
from generate_random_queue import random_queue
from time import time
import graphics


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


time_x = []
time_add_y = []
for i in range(500, 10000, 100):
    data_v = i
    test_add_queue: PriorityQueue = start_testing(i, 'add', data_v)
    ans = (data_v, check_add(test_add_queue))
    print(ans)
    time_x.append(ans[0])
    time_add_y.append(ans[1])

print('-' * 10)

time_extract_y = []
for i in range(500, 10000, 100):
    data_v = i
    test_extract_queue: PriorityQueue = start_testing(i, 'extract', data_v)
    ans = (data_v, check_extract(test_extract_queue))
    print(ans)
    time_extract_y.append(ans[1])

# print(time_x, len(time_x))
# print(time_add_y, len(time_add_y))
# print(time_extract_y, len(time_extract_y))
graphics.paint_grafics(time_x, time_add_y, time_extract_y)
