from collections import deque


class DQ(object):
    def __init__(self):
        self.dq = deque()

    def push(self, x):
        self.dq.append(x)

    def is_empty(self):
        return len(self.dq) == 0


class Stack(DQ):
    def pop(self):
        return self.dq.pop()


class Queue(DQ):
    def pop(self):
        return self.dq.popleft()


def flatmap(function, array):
    return [y for x in map(function, array) for y in x]
