import random
import pandas as pd

from typing import Callable
from priority_queue import PriorityQueue
from generate_random_queue import random_queue
from time import time
import graphics

ATTEMPTS: int = 100

def time_it(function: Callable) -> Callable:
    def wrap_and_time(*args):
        start = time()
        function(*args)
        end = time()
        result = end - start
        return result

    return wrap_and_time


def start_testing(queue_length: int, name_method: str):
    new_queue = random_queue(queue_length, name_method)
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


res = {'size_data': [],
       'add_time': [],
       'extract_time': []}
aver = {'size_data': [],
        'add_average': [],
        'extract_average': []}
time_x = []
time_add_y_average = []
for i in range(500, 10001, 500):
    ans = []
    for attempt in range(ATTEMPTS):
        data_v = i
        test_add_queue: PriorityQueue = start_testing(data_v, 'add')
        time_work = check_add(test_add_queue)
        ans.append(time_work)
        res['add_time'].append(time_work)
        res['size_data'].append(data_v)
    # print(ans)
    time_x.append(data_v)
    aver['size_data'].append(data_v)
    average_ans = sum(ans) / len(ans)
    aver['add_average'].append(average_ans)
    time_add_y_average.append(average_ans)

print('-' * 10)

time_extract_y_average = []
time_linear_algorithm_average = []
for i in range(500, 10001, 500):
    ans = []
    for attempt in range(ATTEMPTS):
        data_v = i
        test_extract_queue: PriorityQueue = start_testing(data_v, 'extract')
        time_work = check_add(test_extract_queue)
        ans.append(time_work)
        res['extract_time'].append(time_work)
    # print(ans)
    average_ans = sum(ans) / len(ans)
    aver['extract_average'].append(average_ans)
    time_extract_y_average.append(average_ans)
graphics.paint_grafics(time_x, time_add_y_average, time_extract_y_average)

res = pd.DataFrame(res)
aver = pd.DataFrame(aver)
salary_sheets = {'Research': res, 'Average': aver}
writer = pd.ExcelWriter('./table.xlsx', engine='xlsxwriter')

for sheet_name in salary_sheets.keys():
    salary_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

writer.save()
