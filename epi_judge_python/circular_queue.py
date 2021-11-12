from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.count = 0
        self.array = [None] * capacity
        self.write = 0
        self.read = 0
        self.__assert_invariants()
        return

    def __assert_invariants(self):
        assert 0 <= self.read < self.capacity
        assert 0 <= self.write < self.capacity
        assert len(self.array) == self.capacity
        return

    def __expand(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.capacity):
            new_array[i] = self.array[(i + self.read) % self.capacity]
        self.read = 0
        self.write = self.capacity
        self.capacity = new_capacity
        self.array = new_array
        self.__assert_invariants()
        return

    def enqueue(self, x: int) -> None:
        if self.size() == self.capacity:
            self.__expand()
        self.array[self.write] = x
        self.write = (self.write + 1) % self.capacity
        self.count += 1
        self.__assert_invariants()
        return

    def dequeue(self) -> int:
        if self.count == 0:
            raise Exception("I'm empty!")
        elt = self.array[self.read]
        self.read = (self.read + 1) % self.capacity
        self.count -= 1
        self.__assert_invariants()
        return elt

    def size(self) -> int:
        self.__assert_invariants()
        return self.count


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    generic_test.generic_test_main('circular_queue.py',
                                   'circular_queue.tsv', queue_tester)
