from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self):
        self.read = []
        self.write = []

    def enqueue(self, x: int) -> None:
        self.write.append(x)
        return

    def __move_elts(self):
        while len(self.write) > 0:
            self.read.append(self.write.pop())

    def dequeue(self) -> int:
        if len(self.read) == 0:
            self.__move_elts()
        return self.read.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
