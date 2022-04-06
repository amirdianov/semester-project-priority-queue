import random

from priority_queue import PriorityQueue
from generate_random_queue import random_queue
from time import time
new_queue: PriorityQueue = PriorityQueue()

def start_testing(idx: int, tests_count: int):
    global new_queue
    new_queue = random_queue(idx, 'add',tests_count)
    return new_queue

def check_add(idx: int, tests_count):
    test_queue: PriorityQueue = start_testing(idx, tests_count)
    queue: PriorityQueue = PriorityQueue()
    start = time()
    for node in test_queue.queue:
        queue.add(node.priority, node.value)
    print(time() - start)

for i in range(1, 6):
    check_add(i, 10 ** i)

#COUNT = 1
#start_testing()
#start_testing()
