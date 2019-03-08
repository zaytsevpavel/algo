# Design a max queue.
# It should support a queue API:
# 1. enqueue should add an element from the queue.
# 2. dequeue should remove an element to the queue.
# 3. is_empty should return true when the queue is empty.
# 4. get_size should return the current size of the queue.
# 5. get_max should return the maximum element currently in the queue.


from collections import deque
import unittest

"""
Code
"""


class MaxQueue:
    def __init__(self):
        self.size = 0
        self.max = None
        self.q = deque()
        self.max_queue = deque()

    def get_max(self):
        if self.is_empty():
            raise ValueError("Max is impossible on the empty queue.")
        return self.max

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __handle_max(self, elem):
        if self.is_empty() or elem >= self.max:
            self.max_queue = deque([elem])
            self.max = elem
        else:
            while self.max_queue and self.max_queue[0] < elem:
                self.max_queue.popleft()
            self.max_queue.appendleft(elem)

    def enqueue(self, elem):
        self.__handle_max(elem)
        self.q.appendleft(elem)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Dequeue is impossible on the empty queue.")
        elem = self.q.pop()
        if self.max_queue and self.max_queue[-1] == elem:
            self.max_queue.pop()
            if self.max_queue:
                self.max = self.max_queue[-1]
            else:
                self.max = None
        self.size -= 1
        return elem


"""
Tests
"""


class TestQueue(unittest.TestCase):
    def test_empty(self):
        """
        Test api on the empty queue
        :return:
        """
        max_queue = MaxQueue()
        with self.assertRaises(ValueError) as context:
            max_queue.get_max()
        self.assertTrue('Max is impossible' in str(context.exception))

        self.assertTrue(max_queue.get_size() == 0)

        with self.assertRaises(ValueError) as context:
            max_queue.dequeue()
        self.assertTrue('Dequeue is impossible' in str(context.exception))

    def test_increasing(self):
        """
        Test that api works for increasing sequence
        :return:
        """
        max_queue = MaxQueue()
        max_queue.enqueue(1)
        self.assertTrue(max_queue.get_max() == 1)
        max_queue.enqueue(2)
        self.assertTrue(max_queue.get_max() == 2)
        max_queue.enqueue(3)
        self.assertTrue(max_queue.size == 3)
        self.assertTrue(max_queue.get_max() == 3)
        elem = max_queue.dequeue()
        self.assertTrue(max_queue.size == 2)
        self.assertTrue(elem == 1)
        next_elem = max_queue.dequeue()
        self.assertTrue(next_elem == 2)
        max_element = max_queue.dequeue()
        self.assertTrue(max_element == 3)
        with self.assertRaises(ValueError) as context:
            max_queue.get_max()
        self.assertTrue("Max is impossible" in str(context.exception))

    def test_decreasing(self):
        """
        Test that api works for decreasing sequence
        :return:
        """
        max_queue = MaxQueue()
        max_queue.enqueue(3)
        max_queue.enqueue(2)
        max_queue.enqueue(1)
        self.assertTrue(max_queue.get_max() == 3)
        elem = max_queue.dequeue()
        self.assertTrue(elem == 3)
        self.assertTrue(max_queue.get_max() == 2)
        elem2 = max_queue.dequeue()
        self.assertTrue(elem2 == 2)
        self.assertTrue(max_queue.get_max() == 1)
        max_queue.dequeue()
        with self.assertRaises(ValueError) as context:
            max_queue.get_max()
        self.assertTrue('Max is impossible' in str(context.exception))

    def test_mixed_workloads(self):
        """
        Test that api works for mixed workloads
        :return:
        """
        max_queue = MaxQueue()
        max_queue.enqueue(5)
        max_queue.enqueue(2)
        max_queue.enqueue(4)
        self.assertTrue(max_queue.get_max() == 5)
        max_queue.dequeue()
        self.assertTrue(max_queue.get_max() == 4)
        self.assertTrue(max_queue.get_size() == 2)
        max_queue.dequeue()
        self.assertTrue(max_queue.get_max() == 4)


if __name__ == '__main__':
    unittest.main()
