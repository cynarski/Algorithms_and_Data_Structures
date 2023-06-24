#Michał Cynarski
# skończone

from math import inf

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return self.key

class Edge:
    def __init__(self, capacity, isresidual):
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity
        self.isresidual = isresidual

    def __str__(self):
        return f"{self.capacity} {self.flow} {self.residual} {self.isresidual}"

    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual} {self.isresidual}"


class GraphList:
    def __init__(self):
        self.neighbour_list = {}
        self.vertex_list = []
        self.vertex_dict = {}

    def insertVertex(self, vertex: Vertex):
        self.vertex_dict[vertex] = self.order()
        self.neighbour_list[self.order()] = []
        self.vertex_list.append(vertex)

    def insertEdge(self, vertex1, vertex2, edge):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.neighbour_list[idx1].append((idx2, edge))
        self.neighbour_list[idx1] = self.neighbour_list[idx1]

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)

        for edge in self.neighbour_list[idx1]:
            if edge[0] == idx2:
                self.neighbour_list[idx1].remove(edge)
                break

    def deleteVertex(self, vertex):
        index = self.getVertexIdx(vertex)
        lst = [i for i in self.neighbour_list[index]]

        for i in lst:
            self.deleteEdge(vertex, self.getVertex(i))

        self.neighbour_list.pop(index)
        self.vertex_dict.pop(vertex)
        self.vertex_list.remove(vertex)

        for i in self.vertex_list:
            self.vertex_dict[i] = self.vertex_list.index(i)

        old_dict = self.neighbour_list.copy()

        for key, value in old_dict.items():
            for i in value:
                if i > index:
                    idx = value.index(i)
                    value[idx] = i - 1
            if key > index:
                self.neighbour_list[key - 1] = value
                self.neighbour_list.pop(key)
            else:
                self.neighbour_list[key] = value

    def getVertexIdx(self, vertex):
        return self.vertex_dict[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighbours(self, vertex_idx):
        return self.neighbour_list[vertex_idx]

    def order(self):
        return len(self.vertex_list)

    def size(self):
        return len(self.edges()) // 2

    def edges(self):
        return [(self.getVertex(key).key, self.getVertex(i).key) for key, values in self.neighbour_list.items() for i in values]

    def getEdge(self, v1, v2):
        for edge in self.neighbour_list[v1]:
            if edge[0] == v2:
                return edge[1]

def BFS(g: GraphList, start):
    visited = []
    parent = [None for _ in range(g.order())]
    Q = [start]
    while Q:
        el = Q.pop(0)
        neighs = g.neighbours(el)
        for u in neighs:
            if u[0] not in visited and g.getEdge(el, u[0]).residual > 0:
                Q.append(u[0])
                visited.append(u[0])
                parent[u[0]] = el
    return parent

def calculate_flow(g: GraphList, start, end, parent):
    current = end
    min_capacity = inf

    if parent[end] is not None:
        while current is not start:
            edge_ = g.getEdge(parent[current], current)
            if min_capacity > edge_.residual:
                min_capacity = edge_.residual
            current = parent[current]

        return min_capacity
    return 0

def path_augmentation(g: GraphList, start, end, parent, min_capacity):
    current = end
    while current is not start:
        g.getEdge(parent[current], current).flow += min_capacity
        g.getEdge(parent[current], current).residual -= min_capacity
        g.getEdge(current, parent[current]).residual += min_capacity

        current = parent[current]

def Ford_Fulkerson(g: GraphList, start, end):
    start = g.getVertexIdx(start)
    end = g.getVertexIdx(end)

    result = 0
    parent = BFS(g,start)
    min_capacity = calculate_flow(g,start, end, parent)
    while min_capacity > 0:
        result += min_capacity
        path_augmentation(g, start, end, parent, min_capacity)
        parent = BFS(g,start)
        min_capacity = calculate_flow(g, start, end, parent)
    return result


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


if __name__ == '__main__':

    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
              ('d', 'c', 4)]

    for lst in [graf_0, graf_1, graf_2, graf_3]:
        graph = GraphList()
        for elem in lst:
            if Vertex(elem[0]) not in graph.vertex_list:
                graph.insertVertex(Vertex(elem[0]))
            if Vertex(elem[1]) not in graph.vertex_list:
                graph.insertVertex(Vertex(elem[1]))
            graph.insertEdge(Vertex(elem[0]), Vertex(elem[1]), Edge(elem[2], False))
            graph.insertEdge(Vertex(elem[1]), Vertex(elem[0]), Edge(0, True))
        print(Ford_Fulkerson(graph,Vertex('s'), Vertex('t')))
        printGraph(graph)
