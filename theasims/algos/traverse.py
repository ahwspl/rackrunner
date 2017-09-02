from itertools import permutations
from random import shuffle
from theasims.algos.search import bfs_parallel, dfs_path, bfs_any_path, bfs_any_path_parallel


def greedy(graph, ordlocs, fast=True):
    pp = graph.pickup_pt
    dp = graph.drop_pt

    ordlocs = set(ordlocs)

    full_path = [pp]
    full_distance = 0
    while len(ordlocs) > 0:
        if fast:
            next_loc, next_path, distance = bfs_any_path(graph, full_path[-1], ordlocs)
        else:
            next_loc, next_path, distance = bfs_any_path_parallel(graph, full_path[-1], ordlocs)
        full_path = full_path + next_path[1:]
        full_distance = full_distance + distance
        ordlocs.remove(next_loc)

    next_path, distance = bfs_parallel(graph, full_path[-1], dp)
    full_path = full_path + next_path[1:]
    full_distance = full_distance + distance

    return full_path, full_distance


def lexicographic(graph, ordlocs, fast=True):
    pp = graph.pickup_pt
    dp = graph.drop_pt

    aisles = sorted(list(set(map(lambda x: x.aisle, ordlocs))))

    full_path = [pp]
    full_distance = 0
    for aisle in aisles:
        subset = set(filter(lambda x: x.aisle == aisle, ordlocs))
        while len(subset) > 0:
            if fast:
                next_loc, next_path, distance = bfs_any_path(graph, full_path[-1], subset)
            else:
                next_loc, next_path, distance = bfs_any_path_parallel(graph, full_path[-1], subset)
            full_path = full_path + next_path[1:]
            full_distance = full_distance + distance
            subset.remove(next_loc)

    next_path, distance = bfs_parallel(graph, full_path[-1], dp)
    full_path = full_path + next_path[1:]
    full_distance = full_distance + distance

    return full_path, full_distance


def ord_path(graph, ordlocs, cap=-1, randpath=False):
    pp = graph.pickup_pt
    dp = graph.drop_pt

    if cap == -1:
        cap = graph.maxlim

    plan = [pp] + ordlocs + [dp]

    full_path = [pp]
    full_distance = 0
    for i in range(len(plan) - 1):
        if randpath:
            next_path, distance = dfs_path(graph, plan[i], plan[i + 1], True)
        else:
            next_path, distance = bfs_parallel(graph, plan[i], plan[i + 1], cap - full_distance)

        if next_path is None:
            return None, None

        full_path = full_path + next_path[1:]
        full_distance = full_distance + distance

    return full_path, full_distance


def strict_lexicographic(graph, ordlocs):
    ordlocs = sorted(ordlocs)
    return ord_path(graph, ordlocs)


def rand_ord_path(graph, ordlocs):
    ordlocs = list(ordlocs)
    shuffle(ordlocs)
    return ord_path(graph, ordlocs)


def rand_ord_rand_path(graph, ordlocs):
    ordlocs = list(ordlocs)
    shuffle(ordlocs)
    return ord_path(graph, ordlocs, randpath=True)


def brute_force(graph, ordlocs, limit=-1, maxlimct=3):
    possibilities = []
    limit_count = 0
    for perm in permutations(ordlocs):
        path, distance = ord_path(graph, list(perm), limit)
        if path is None:
            continue
        possibilities.append((path, distance))
        if distance < limit:
            break
        elif distance == limit:
            limit_count += 1
            if limit_count >= maxlimct:
                # print("Warn: Brute Count limit reached!")
                break

    if possibilities:
        return min(possibilities, key=lambda tup: tup[1])
    else:
        return None, None


# Example Strategies

def brute_greedy(graph, ordlocs):
    greedy_path, greedy_dist = greedy(graph, ordlocs)
    brute_path, brute_dist = brute_force(graph, ordlocs, greedy_dist)
    if brute_path is None:
        print("Warn: Brute -> Greedy")
        return greedy_path, greedy_dist
    return brute_path, brute_dist


def brute_5(graph, ordlocs):
    if len(ordlocs) <= 5:
        return brute_greedy(graph, ordlocs)
    else:
        return greedy(graph, ordlocs)


def brute_9(graph, ordlocs):
    if len(ordlocs) <= 9:
        return brute_greedy(graph, ordlocs)
    else:
        return greedy(graph, ordlocs)


def brute_14(graph, ordlocs):
    if len(ordlocs) <= 14:
        return brute_greedy(graph, ordlocs)
    else:
        return greedy(graph, ordlocs)
