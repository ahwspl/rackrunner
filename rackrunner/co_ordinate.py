from theasims.algos import dsa
from theasims.maps.thea2 import thea2

#getpath import
from theasims.maps.structures import Location
from theasims.algos.traverse import greedy

def get_coordinate():
    flatmap_of_list = (dsa.flatmap(thea2.get_neighbors, thea2.locations))
    flatmap_of_list = [dict(zip(('x', 'y'), (i.x, i.y))) for i in flatmap_of_list]
    map_location = [i.label for i in thea2.locations]
    return dict(zip(map_location, flatmap_of_list))


def get_boundary():
    return {
        "length": thea2.length,
        "width": thea2.width
    }

def get_path(racks):
    if racks is None or len(racks) == 0:
        return []
    print(type(racks))
    print(racks)
    flatmap_of_list = (dsa.flatmap(thea2.get_neighbors, thea2.locations))
    flatmap_of_list = [dict(zip(('x', 'y'), (i.x, i.y))) for i in flatmap_of_list]
    map_location = [i.label for i in thea2.locations]
    label_to_location_mapping = dict(zip(map_location, flatmap_of_list))

    orderobj = list(map(Location, racks))
    a = greedy(thea2, orderobj)

    result = []
    for point in a[0]:
        if type(point) is Location:
            temp = label_to_location_mapping[point.label]
            temp['isPickUp'] = True
            result.append(temp)
        else:
            result.append({"x": point.x, "y": point.y, "isPickUp": False})

    return result