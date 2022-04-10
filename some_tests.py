"""
import unittest
from priority_queue import PriorityQueue, QueueNode
from abc import ABC
from random import randint

def keys(priority_queue: PriorityQueue) -> list:
    return [node.priority for node in priority_queue.queue]

def add_values_into_queue(queue: PriorityQueue, nodes: list[int]) -> None:
    for priority in nodes:
        queue.add(priority, randint(-10000, 10000))

class TestMethods(ABC, unittest.TestCase):
    def setUp(self) -> None:
        self.test_queue : PriorityQueue = PriorityQueue()

class TestAddMethod(TestMethods):
    def test1(self):
        add_values_into_queue(self.test_queue, [1, 2, 3, 4, 5])
        self.assertEqual(keys(self.test_queue), [5, 4, 2, 1, 3])

    def test2(self):
        add_values_into_queue(self.test_queue, [1, 3])
        self.assertEqual(keys(self.test_queue), [3, 1])

    def test3(self):
        add_values_into_queue(self.test_queue, [15, 16, 20, 15])
        self.assertEqual(keys(self.test_queue), [20, 15, 16, 15])

    def test4(self):
        add_values_into_queue(self.test_queue, [20, 16, 15, 15])
        self.assertEqual(keys(self.test_queue), [20, 16, 15, 15])

    def test5(self):
        add_values_into_queue(self.test_queue, [-2, 10, 15])
        self.assertEqual(keys(self.test_queue), [15, -2, 10])

class TestExtractMethod(TestMethods):
    def test1(self):
        add_values_into_queue(self.test_queue, [5])
        value: int = self.test_queue.queue[0].value
        self.assertEqual(self.test_queue.extract(), value)
        self.assertEqual(0, len(self.test_queue))

    def test2(self):
        add_values_into_queue(self.test_queue, [5, 4])
        value: int = self.test_queue.queue[0].value
        self.assertEqual(self.test_queue.extract(), value)
        self.assertEqual(1, len(self.test_queue))
        value: int = self.test_queue.queue[0].value
        self.assertEqual(self.test_queue.extract(), value)
        self.assertEqual(0, len(self.test_queue))"""