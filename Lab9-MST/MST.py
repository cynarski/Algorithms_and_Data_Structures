#Michał Cynarski
# skończone

from math import inf
import graf_mst

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
    def __init__(self, vertex1, vertex2, weight=1):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight



class GraphList:
    def __init__(self):
        self.neighbour_list = dict()
        self.vertex_list = []
        self.vertex_dict = dict()
        self.edges = []
        self.get_weight = dict()

    def insertVertex(self, vertex):
        self.vertex_list.append(vertex)
        idx = self.vertex_list.index(vertex)
        self.neighbour_list[vertex] = idx
        self.vertex_dict[idx] = []

    def insertEdge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list and vertex1 != vertex2:
            idx1 = self.getVertexIdx(vertex1)
            idx2 = self.getVertexIdx(vertex2)
            if idx1 not in self.vertex_dict[idx2] or idx2 not in self.vertex_dict[idx1]:
                self.vertex_dict[idx1].append(idx2)
                self.vertex_dict[idx1].sort()

                self.vertex_dict[idx2].append(idx1)
                self.vertex_dict[idx2].sort()
            self.edges.append(Edge(vertex1, vertex2, weight))
            self.get_weight[(idx1, idx2)] = weight

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

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)

        self.neighbour_list[idx1].remove(idx2)
        self.neighbour_list[idx2].remove(idx1)

    def getVertexIdx(self, vertex):
        return self.neighbour_list[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighbours(self, vertex_idx):
        lst = self.vertex_dict[vertex_idx]
        new = []
        for p in lst:
            new.append((p, self.get_weight[(vertex_idx, p)]))
        return new

    def size(self):
        return len(self.list_of_edges())

    def list_of_edges(self):
        lista = []
        for k, v in self.vertex_dict.items():
            for i in v:
                lista.append((self.getVertex(k).key, self.getVertex(i).key))
        return lista

    def order(self):
        return len(self.vertex_dict)

def MST(G: GraphList):
    length = 0
    intree = [0] * G.order()
    distance = [inf] * G.order()
    parent = [-1] * G.order()

    newG = GraphList()

    for ve in G.list_of_edges():
        if Vertex(ve[0]) not in newG.neighbour_list.keys():
            newG.insertVertex(Vertex(ve[0]))
        if Vertex(ve[1]) not in newG.neighbour_list.keys():
            newG.insertVertex(Vertex(ve[1]))

    v = 0
    distance[v] = 0
    while intree[v] == 0:
        intree[v] = 1
        length += distance[v]
        for ver in G.neighbours(v):
            if ver[1] < distance[ver[0]] and intree[ver[0]] == 0:
                distance[ver[0]] = ver[1]
                parent.pop(ver[0])
                parent.insert(ver[0], v)

        minimum = inf
        for idx in range(len(intree)):
            if intree[idx] == 0:
                if distance[idx] < minimum:
                    minimum = distance[idx]
                    v = idx

        newG.insertEdge(newG.getVertex(parent[v]), newG.getVertex(v), distance[v])
        newG.insertEdge(newG.getVertex(v), newG.getVertex(parent[v]), distance[v])

    return newG, length

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
    graph = GraphList()
    for i in graf_mst.graf:
        if Vertex(i[0]) not in graph.neighbour_list.keys():
            graph.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in graph.neighbour_list.keys():
            graph.insertVertex(Vertex(i[1]))
        graph.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        graph.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    new, leng = MST(graph)
    printGraph(new)