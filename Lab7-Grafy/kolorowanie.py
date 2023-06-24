#Michał Cynarski
# skończone

import polska


class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

class Edge:
    pass

class GraphMatrix:
    def __init__(self):
        self.matrix = []
        self.vertex_list = []
        self.vertex_dict = {}

    def is_empty(self):
        return True if len(self.vertex_list) == 0 else False

    def insertVertex(self, vertex):
        self.vertex_list.append(vertex)
        idx = self.vertex_list.index(vertex)
        self.vertex_dict[vertex] = idx
        self.matrix.append([0] * len(self.vertex_list))
        for i in range(len(self.vertex_list) - 1):
            self.matrix[i].append(0)

    def insertEdge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list and vertex1 != vertex2:

            idx1 = self.getVertexIdx(vertex1)
            idx2 = self.getVertexIdx(vertex2)

            self.matrix[idx1][idx2] = 1
            self.matrix[idx2][idx1] = 1

    def deleteVertex(self, vertex):
        index = self.getVertexIdx(vertex)
        idx = 0

        for i in self.matrix[index]:
            if i == 1:
                self.deleteEdge(vertex,self.vertex_list[idx])
            idx += 1
        self.matrix.pop(index)
        self.vertex_list.pop(index)
        self.vertex_dict.pop(vertex)

        for i in range(len(self.vertex_list)):
            self.matrix[i].pop(index)
            self.vertex_dict[self.vertex_list[i]] = i

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list and vertex1 != vertex2:
            idx1 = self.getVertexIdx(vertex1)
            idx2 = self.getVertexIdx(vertex2)

            self.matrix[idx1][idx2] = 0
            self.matrix[idx2][idx1] = 0

    def getVertexIdx(self, vertex):
        return self.vertex_dict[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighbours(self, vertex_id):
        return [idx for idx, i in enumerate(self.matrix[vertex_id]) if i == 1]

    def order(self):
        return len(self.vertex_list)

    def size(self):
        return sum(sum(i) for i in self.matrix) // 2

    def edges(self):
        return [(i.key, self.getVertex(j).key) for i in self.vertex_list for j in self.neighbours(self.getVertexIdx(i))]

class GraphList:
    def __init__(self):
        self.neighbour_list = {}
        self.vertex_list = []
        self.vertex_dict = {}

    def is_empty(self):
        return True if len(self.vertex_list) == 0 else False

    def insertVertex(self, vertex):
        self.vertex_list.append(vertex)
        idx = self.vertex_list.index(vertex)
        self.vertex_dict[vertex] = idx
        self.neighbour_list[idx] = []

    def insertEdge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list and vertex1 != vertex2:

            idx1 = self.getVertexIdx(vertex1)
            idx2 = self.getVertexIdx(vertex2)

            if idx1 not in self.neighbour_list[idx2] or idx2 not in self.neighbour_list[idx1]:
                self.neighbour_list[idx1].append(idx2)
                self.neighbour_list[idx2].append(idx1)

                self.neighbour_list[idx1].sort()
                self.neighbour_list[idx2].sort()

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
        return self.vertex_dict[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighbours(self, vertex_id):
        return self.neighbour_list[vertex_id]

    def order(self):
        return len(self.vertex_list)

    def size(self):
        return len(self.edges()) // 2

    def edges(self):
        return [(self.getVertex(key).key, self.getVertex(i).key) for key, values in self.neighbour_list.items() for i in values]

def DFS(graph, start=0):
    lst = ['0', '1', '2', '3', '4', '5', '6', '7']
    colors = dict()
    visited = list()
    queue = [start]
    while queue:
        a = lst.copy()
        start = queue.pop()
        if start not in visited:
            visited.append(start)

            for n in graph.neighbours(start):
                if n in colors.keys():
                    if colors[n] in a:
                        a.remove(colors[n])

            colors[start] = a[0]

            for i in graph.neighbours(start)[::-1]:
                queue.append(i)
    return colors

def BFS(graph, start=0):
    lst = ['0', '1', '2', '3', '4', '5', '6', '7']
    visited = list()
    colors = dict()
    colors[start] = '1'
    queue = [start]
    visited.append(start)
    while queue:
        start = queue.pop(0)

        for n in graph.neighbours(start):
            a = lst.copy()
            if n not in visited:
                visited.append(n)
                queue.append(n)
                for i in graph.neighbours(n):
                    if i in colors.keys():
                        if colors[i] in a:
                            a.remove(colors[i])
                colors[n] = a[0]
    return colors

def kolorowanie(graph, type):
    lista = []

    if type == 'DFS':
        path = DFS(graph)

    elif type == 'BFS':
        path = BFS(graph)

    for k, v in path.items():
        lista.append((graph.getVertex(k).key, v))

    polska.draw_map(graph.edges(), lista)


if __name__ == '__main__':

    graph_list = GraphList()
    graph_matrix = GraphMatrix()

    for vertex in polska.polska:
        graph_list.insertVertex(Vertex(vertex[2]))
        graph_matrix.insertVertex(Vertex(vertex[2]))

    for edge in polska.graf:
        graph_list.insertEdge(Vertex(edge[0]),Vertex(edge[1]))
        graph_matrix.insertEdge(Vertex(edge[0]),Vertex(edge[1]))

    kolorowanie(graph_matrix, 'BFS')