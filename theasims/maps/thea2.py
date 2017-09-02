from itertools import product

from theasims.maps.structures import Graph, Location, ExtPt


def make_ext(x, y):
    return ExtPt(str(x).zfill(2) + str(y).zfill(2))


def make_loc(a, n):
    return Location(a + str(n).zfill(2))


def generate_thea2():
    ext_x = 28
    ext_y = 52
    lanes = 9
    laneWidth = 6
    x_unit = 3
    y_unit = 1
    loc2x = 2
    pick_dist = 6

    aisles = {'A': 24, 'B': 48, 'C': 48, 'D': 48, 'E': 48, 'F': 48, 'G': 48, 'H': 48, 'I': 50, 'R': 7}

    locations = []
    for prefix in sorted(aisles):
        count = aisles[prefix]
        for i in range(1, count + 1):
            locations.append(make_loc(prefix, i))

    ext_points = [make_ext(x, y) for (x, y) in product(range(0, ext_x), range(0, ext_y))]

    pickup_point = ExtPt('9999')

    maxlim = ((ext_x - 1) * x_unit * lanes
              + (lanes - 1) * laneWidth
              + len(locations) * loc2x
              - aisles['R'] * loc2x / 2
              + pick_dist) * 2 + 1

    g = Graph(locations + ext_points + [pickup_point], pickup_point, pickup_point, maxlim)

    # Pickup-Drop
    g.add_edge(pickup_point, make_ext(0, 7), pick_dist)
    g.add_edge(pickup_point, make_ext(0, 13), pick_dist)

    # Horizontal
    for y in range(1, ext_y, laneWidth):
        for x in range(0, ext_x - 1):
            g.add_edge(make_ext(x, y), make_ext(x + 1, y), x_unit)

    # Vertical
    for x in [0, 13, 14, 27]:
        for y in range(1, ext_y - 3, laneWidth):
            g.add_edge(make_ext(x, y), make_ext(x, y + laneWidth), laneWidth)

    # Aisle A
    for number in range(1, 13):
        x = number
        g.add_edge(make_loc('A', number), make_ext(x, 1 + loc2x), 0)
        g.add_edge(make_ext(x, 1), make_ext(x, 1 + loc2x), loc2x)

    for number in range(13, 25):
        x = number + 2
        g.add_edge(make_loc('A', number), make_ext(x, 1 + loc2x), 0)
        g.add_edge(make_ext(x, 1), make_ext(x, 1 + loc2x), loc2x)

    # Aisles B to H
    for aisle, y in zip(['B', 'C', 'D', 'E', 'F', 'G', 'H'], list(range(7, ext_y, laneWidth))):
        for number in range(2, 25, 2):
            x = int(number / 2)
            g.add_edge(make_loc(aisle, number - 1), make_ext(x, y - loc2x), 0)
            g.add_edge(make_ext(x, y), make_ext(x, y - loc2x), loc2x)
            g.add_edge(make_loc(aisle, number), make_ext(x, y + loc2x), 0)
            g.add_edge(make_ext(x, y), make_ext(x, y + loc2x), loc2x)

        for number in range(26, 49, 2):
            x = int(number / 2) + 2
            g.add_edge(make_loc(aisle, number - 1), make_ext(x, y - loc2x), 0)
            g.add_edge(make_ext(x, y), make_ext(x, y - loc2x), loc2x)
            g.add_edge(make_loc(aisle, number), make_ext(x, y + loc2x), 0)
            g.add_edge(make_ext(x, y), make_ext(x, y + loc2x), loc2x)

    # Aisle I
    for number in range(2, 25, 2):
        x = int(number / 2)
        g.add_edge(make_loc('I', number - 1), make_ext(x, 49 - loc2x), 0)
        g.add_edge(make_ext(x, 49), make_ext(x, 49 - loc2x), loc2x)
        g.add_edge(make_loc('I', number), make_ext(x, 49 + loc2x), 0)
        g.add_edge(make_ext(x, 49), make_ext(x, 49 + loc2x), loc2x)

    g.add_edge(make_loc('I', 25), make_ext(13, 49 + loc2x), 0)
    g.add_edge(make_ext(13, 49), make_ext(13, 49 + loc2x), loc2x)
    g.add_edge(make_loc('I', 26), make_ext(14, 49 + loc2x), 0)
    g.add_edge(make_ext(14, 49), make_ext(14, 49 + loc2x), loc2x)

    for number in range(28, 51, 2):
        x = int(number / 2) + 1
        g.add_edge(make_loc('I', number - 1), make_ext(x, 49 - loc2x), 0)
        g.add_edge(make_ext(x, 49), make_ext(x, 49 - loc2x), loc2x)
        g.add_edge(make_loc('I', number), make_ext(x, 49 + loc2x), 0)
        g.add_edge(make_ext(x, 49), make_ext(x, 49 + loc2x), loc2x)

    # Refrigerators, have more depth so distance from path = 1
    g.add_edge(make_loc('R', 1), make_ext(15, 0), 0)
    g.add_edge(make_ext(15, 1), make_ext(15, 0), loc2x / 2)
    g.add_edge(make_loc('R', 2), make_ext(16, 0), 0)
    g.add_edge(make_ext(16, 1), make_ext(16, 0), loc2x / 2)
    g.add_edge(make_loc('R', 3), make_ext(17, 0), 0)
    g.add_edge(make_ext(17, 1), make_ext(17, 0), loc2x / 2)
    g.add_edge(make_loc('R', 4), make_ext(18, 0), 0)
    g.add_edge(make_ext(18, 1), make_ext(18, 0), loc2x / 2)
    g.add_edge(make_loc('R', 5), make_ext(19, 0), 0)
    g.add_edge(make_ext(19, 1), make_ext(19, 0), loc2x / 2)
    g.add_edge(make_loc('R', 6), make_ext(20, 0), 0)
    g.add_edge(make_ext(20, 1), make_ext(20, 0), loc2x / 2)
    g.add_edge(make_loc('R', 7), make_ext(21, 0), 0)
    g.add_edge(make_ext(21, 1), make_ext(21, 0), loc2x / 2)

    g.set_parameter(ext_x, ext_y)

    return g

thea2 = generate_thea2()
