from random import shuffle
from theasims.algos.dsa import Stack, Queue, flatmap


# Hypothesis: Gives best path from A to B because of the triangular inequality and symmetry of thea2.
def bfs_path(graph, src, dest, lim=-1):
    if src not in graph or dest not in graph:
        return None, None

    q = Queue()
    q.push(([src], 0))
    while not q.is_empty():
        path, distance = q.pop()

        if lim != -1 and distance > lim:
            # print("Warn: Graph limit reached:", path, distance, lim)
            continue

        current = path[-1]

        if current == dest:
            return path, distance

        for nxt in graph[current]:
            if nxt not in path:
                q.push((path + [nxt], distance + graph[current][nxt]))

    return None, None


def bfs_parallel(graph, src, dest, lim=-1):
    if src not in graph or dest not in graph:
        return None, None

    def makestep(tuple):
        path = tuple[0]
        distance = tuple[1]
        current = path[-1]

        neighbors = graph[current].keys()
        forward = filter(lambda node: node not in path, neighbors)
        tups = map(lambda node: (path + [node], distance + graph[current][node]), forward)
        limited = filter(lambda tup: lim == -1 or tup[1] <= lim, tups)

        return limited

    paths = [([src], 0)]

    while paths:
        test = list(filter(lambda tup: tup[0][-1] == dest, paths))
        if test:
            res = min(test, key=lambda tup: tup[1])
            return res[0], res[1]
        paths = flatmap(makestep, paths)

    return None, None


def bfs_any_path(graph, src, locs):
    if src not in graph or any(loc not in graph for loc in locs):
        print("Unknown Dests: ", list(filter(lambda loc: loc not in graph, locs)))
        return None, None, None

    q = Queue()
    q.push(([src], 0))
    while not q.is_empty():
        path, distance = q.pop()

        current = path[-1]

        if current in locs:
            return current, path, distance

        for nxt in graph[current]:
            if nxt not in path:
                q.push((path + [nxt], distance + graph[current][nxt]))

    return None, None, None


def bfs_any_path_parallel(graph, src, locs):
    if src not in graph or any(loc not in graph for loc in locs):
        return None, None, None

    def makestep(tuple):
        path, distance = tuple

        current = path[-1]

        neighbors = filter(lambda node: node not in path, graph[current].keys())
        tups = map(lambda node: (path + [node], distance + graph[current][node]), neighbors)

        return tups

    paths = [([src], 0)]

    while paths:
        test = list(filter(lambda tup: tup[0][-1] in locs, paths))
        if test:
            res = min(test, key=lambda tup: tup[1])
            return res[0][-1], res[0], res[1]
        paths = flatmap(makestep, paths)

    return None, None, None


# Won't necessarily give the shortest path
def dfs_path(graph, src, dest, rand=False):
    if src not in graph or dest not in graph:
        return None, None

    s = Stack()
    s.push(([src], 0))
    while not s.is_empty():
        path, distance = s.pop()

        current = path[-1]

        if current == dest:
            return path, distance

        neighbors = graph.get_neighbors(current)
        if rand:
            shuffle(neighbors)

        for nxt in neighbors:
            if nxt not in path:
                s.push((path + [nxt], distance + graph[current][nxt]))

    return None, None
