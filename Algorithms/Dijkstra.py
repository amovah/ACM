# really hate python for this bad implement

from math import inf

class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, id, weight):
        self.neighbors.append({
            'id': id,
            'weight': weight
        })

    def get_weight(self, id):
        for neighbor in neighbors:
            if neighbor['id'] == id:
                return neighbor['weight']

        return None


class Graph:
    def __init__(self):
        self.vertices = []
        self.lastId = 0

    def add_vertex(self):
        vertex = Vertex(self.lastId)
        self.vertices.append(vertex)
        self.lastId = self.lastId + 1

        return vertex

    def get_vertex(self, id):
        for vertex in self.vertices:
            if str(vertex.id) == str(id):
                return vertex

        return None

    def add_connection(self, source, target, weight):
        vertex = self.get_vertex(source)
        if vertex is not None:
            vertex.add_neighbor(target, weight)


g = Graph()
def createVertices():
    a = g.add_vertex()
    b = g.add_vertex()
    c = g.add_vertex()
    d = g.add_vertex()
    e = g.add_vertex()
    f = g.add_vertex()

    g.add_connection(a.id, b.id, 7)
    g.add_connection(a.id, c.id, 9)
    g.add_connection(a.id, f.id, 14)
    g.add_connection(b.id, c.id, 10)
    g.add_connection(b.id, d.id, 15)
    g.add_connection(b.id, a.id, 7)
    g.add_connection(c.id, d.id, 11)
    g.add_connection(c.id, f.id, 2)
    g.add_connection(c.id, a.id, 9)
    g.add_connection(c.id, b.id, 10)
    g.add_connection(d.id, b.id, 15)
    g.add_connection(d.id, c.id, 11)
    g.add_connection(e.id, f.id, 9)
    g.add_connection(e.id, d.id, 6)
    g.add_connection(f.id, e.id, 9)
    g.add_connection(f.id, c.id, 2)
    g.add_connection(f.id, a.id, 14)

createVertices()

def findItem(items, id):
    for item in items:
        if item['id'] == id:
            return item

    return None

def dijkstra(g, source, target):
    queue = []
    dist = []
    prev = []

    # initializing
    for vertex in g.vertices:
        dist.append({
            'id': vertex.id,
            'dist': inf
        })
        prev.append({
            'id': vertex.id,
            'prev': None
        })
        queue.append(vertex)

    # set source node dist 0
    findItem(dist, source.id)['dist'] = 0

    # algorithm
    while len(queue):
        # finding a vertex that has min dist value
        # and call it u
        u = dist[0]
        uIndex = 0
        for i in range(len(queue)):
            found = findItem(dist, queue[i].id)
            if found['dist'] < u['dist']:
                u = found
                uIndex = i
        u = queue[uIndex]
        del queue[uIndex]

        # get neighbors
        for neighbor in u.neighbors:
            found = findItem(dist, u.id)
            alt = found['dist'] + neighbor['weight']
            if alt < findItem(dist, neighbor['id'])['dist']:
                found['dist'] = alt
                findItem(prev, neighbor['id'])['prev'] = u

dijkstra(g, g.get_vertex('0'), g.get_vertex('4'))
