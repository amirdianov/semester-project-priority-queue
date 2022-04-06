from generate_random_queue import *


def start_testing():
    global COUNT
    new_queue = random_queue(COUNT)
    print(new_queue)
    COUNT += 1


COUNT = 1
start_testing()
start_testing()
