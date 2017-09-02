from theasims.algos import dsa
from theasims.maps.thea2 import thea2


def get_coordinate():
    flatmap_of_list = (dsa.flatmap(thea2.get_neighbors, thea2.locations))
    flatmap_of_list = [dict(zip(('x', 'y'), (i.x, i.y))) for i in flatmap_of_list]
    map_location = thea2.locations
    return dict(zip(map_location, flatmap_of_list))
