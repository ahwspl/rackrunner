from theasims.algos.dsa import flatmap
from theasims.maps.thea2 import thea2
from theasims.maps.structures import Location
from theasims.algos.traverse import greedy_lex as getpath


def get_coordinate():
    flatmap_of_list = flatmap(thea2.get_neighbors, thea2.locations)
    coords = [dict(zip(('x', 'y'), (i.x, i.y))) for i in flatmap_of_list]
    map_location = [i.label for i in thea2.locations]
    return dict(zip(map_location, coords))


def get_boundary():
    return {
        "length": thea2.length,
        "width": thea2.width
    }


def get_path(racks):
    if racks is None or len(racks) == 0:
        return []

    label_to_location_mapping = get_coordinate()

    orderobj = list(map(Location, racks))
    path, distance = getpath(thea2, orderobj)

    pickup_counter = 1
    result = []

    pre_x = None
    pre_y = None

    delta_x = 0
    delta_y = 0

    for point in path:
        if type(point) is Location:
            temp = label_to_location_mapping[point.label]
            temp['isPickUp'] = True
            temp['counter'] = pickup_counter
            pickup_counter += 1
            result.append(temp)
            pre_x = temp['x']
            pre_y = temp['y']
        else:
            if pre_x is not None:
                if pre_x > point.x:
                    delta_x = 0
                    delta_y = 0.2
                elif pre_x < point.x:
                    delta_x = 0
                    delta_y = -0.2
                elif pre_y > point.y:
                    delta_x = 0.2
                    delta_y = 0
                elif pre_y < point.y:
                    delta_x = -0.2
                    delta_y = 0
            result.append({"x": point.x + delta_x, "y": point.y + delta_y, "isPickUp": False})
            pre_x = point.x
            pre_y = point.y

    del result[0]
    del result[-1]
    start_point = {"x": 0, "y": 1, "isPickUp": False}
    result = [start_point] + result + [start_point]
    return result
