from queue import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PathUtil:

    @staticmethod
    def get_optimal_path(matrix, src, dest):
        q = Queue()
        q.put(src)

        while









