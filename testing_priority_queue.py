import unittest
from priority_queue import PriorityQueue
from random import randint


class TestPriorityQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.pq = PriorityQueue()

    def test_add(self):
        for _ in range(100):
            random_num = randint(1, 1000)
            self.pq.add(random_num, random_num)
            self.assertEqual(random_num, self.pq.search(random_num))

    def test_extract(self):
        data_to_compare = set()
        while len(self.pq) != 100:
            random_num = randint(1, 1000)
            if random_num not in data_to_compare:
                self.pq.add(random_num, random_num)
                data_to_compare.add(random_num)
        for _ in range(100):
            root = self.pq.get_root()
            self.pq.extract()
            self.assertRaises(KeyError, lambda: self.pq.search(root.priority))


if __name__ == '__main__':
    unittest.main()
