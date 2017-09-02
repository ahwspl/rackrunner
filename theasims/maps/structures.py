
class Node(object):
    label = None

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        return self.label < other.label

    def __repr__(self):
        return self.label


class Location(Node):
    def __init__(self, label):
        self.label = label[0:3]
        self.aisle = self.label[0]
        self.number = int(self.label[1:3])


class ExtPt(Node):
    def __init__(self, label):
        self.label = label[0:4]
        self.x = int(self.label[0:2])
        self.y = int(self.label[2:4])


class Graph(object):
    def __init__(self, nodes, pickup_pt, drop_pt=None, maxlim=1e6):
        self.adjList = {}
        for node in nodes:
            self.adjList[node] = {}

        self.pickup_pt = pickup_pt

        if drop_pt:
            self.drop_pt = drop_pt
        else:
            self.drop_pt = self.pickup_pt

        self.maxlim = maxlim

    def __getitem__(self, node):
        return self.adjList[node]

    def __contains__(self, node):
        return node in self.adjList

    def __iter__(self):
        return iter(self.adjList)

    @property
    def nodes(self):
        return sorted(list(self.adjList.keys()))

    @property
    def locations(self):
        return sorted(list(filter(lambda node: isinstance(node, Location), self.adjList.keys())))

    @property
    def ex_points(self):
        return sorted(list(filter(lambda node: isinstance(node, ExtPt), self.adjList.keys())))

    def add_edge(self, node1, node2, distance):
        # print(node1.label + " <-" + str(distance) + "-> " + node2.label)
        self.adjList[node1][node2] = distance
        self.adjList[node2][node1] = distance

    def get_neighbors(self, node):
        return list(self.adjList[node].keys())

    def print(self):
        print(self.adjList)

    def set_parameter(self, width, length):
        self.width = width
        self.length = length
