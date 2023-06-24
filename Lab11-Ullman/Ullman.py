#Michał Cynarski
#skończone

import numpy as np
from copy import deepcopy

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
        if vertex_id < 0 or vertex_id >= len(self.matrix):
            return []
        return [idx for idx, i in enumerate(self.matrix[vertex_id]) if i == 1]

    def order(self):
        return len(self.vertex_list)

    def size(self):
        return sum(sum(i) for i in self.matrix) // 2

    def edges(self):
        return [(i.key, self.getVertex(j).key) for i in self.vertex_list for j in self.neighbours(self.getVertexIdx(i))]

    def display(self):
        print("--------------------")
        for row in self.matrix:
            print(row)
        print("--------------------")

def ullman(G, P, M, used_columns=[], current_row=0, solutions=0, iteration=1):
    if current_row == M.shape[0]:
        return (solutions + 1, iteration) if np.array_equal(P, np.dot(M, np.transpose(np.dot(M, G)))) else (solutions, iteration)

    M_prim = deepcopy(M)

    for c in range(M_prim.shape[1]):
        if c not in used_columns:
            M_prim[current_row] = [0] * M_prim.shape[1]
            M_prim[current_row][c] = 1
            used_columns.append(c)
            solutions, iteration = ullman(G, P, M_prim, used_columns, current_row + 1, solutions, iteration)
            used_columns.pop()
            iteration += 1

    return solutions, iteration

def ullman_2(G, P, M0, M, used_columns=[], current_row=0, solutions=0, iteration=1):
    if current_row == M.shape[0]:
        return (solutions + 1, iteration) if (P == (M @ np.transpose(M @ G))).all() else (solutions, iteration)

    M_prim = deepcopy(M)

    for c in range(M_prim.shape[1]):
        if c not in used_columns and M0[current_row][c] == 1:
            M_prim[current_row] = [0] * M_prim.shape[1]
            M_prim[current_row][c] = 1
            used_columns.append(c)
            solutions, iteration = ullman_2(G, P, M0, M_prim, used_columns, current_row + 1, solutions, iteration)
            used_columns.pop()
            iteration += 1

    return solutions, iteration

def prune(G, P, M):
    indexes = [(i, j) for i in range(M.shape[0]) for j in range(M.shape[1]) if M[i][j] == 1]
    change = True
    while change:
        change = False
        for i, j in indexes:
            neighboursP = [k for k in range(len(P[i])) if P[i][k] == 1]
            neighboursG = [k for k in range(len(G[j])) if G[j][k] == 1]
            exist = False
            for x in neighboursP:
                for y in neighboursG:
                    if M[x][y] == 1:
                        exist = True
                        break
                if exist:
                    break
            if not exist:
                change = True
                M[i][j] = 0
                indexes.remove((i, j))


def ullman_3(G, P, M0, M, used_columns=[], current_row=0, solutions=0, iteration=1):
    if current_row == M.shape[0]:
        return (solutions + 1, iteration) if (P == (M @ np.transpose(M @ G))).all() else (solutions, iteration)

    M_prim = deepcopy(M)
    if current_row == M.shape[0] - 1:
        prune(G,P,M_prim)
    if current_row >= 1:
        for row in M_prim[:current_row]:
            if row.sum() == 0:
                return solutions,iteration
    for c in range(M_prim.shape[1]):
        if c not in used_columns:
            if M0[current_row][c] == 1:
                for i in range(M_prim.shape[1]):
                    M_prim[current_row][i] = 0
                M_prim[current_row][c] = 1
                used_columns.append(c)
                solutions, iteration = ullman_3(G, P, M0, M_prim, used_columns, current_row + 1, solutions, iteration)
                used_columns.pop()
                iteration += 1

    return solutions, iteration


if __name__ == '__main__':
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
    g1 = GraphMatrix()
    g2 = GraphMatrix()

    for elem in graph_G:
        if Vertex(elem[0]) not in g1.vertex_list:
            g1.insertVertex(Vertex(elem[0]))
        if Vertex(elem[1]) not in g1.vertex_list:
            g1.insertVertex(Vertex(elem[1]))
        g1.insertEdge(Vertex(elem[0]), Vertex(elem[1]))

    for elem in graph_P:
        if Vertex(elem[0]) not in g2.vertex_list:
            g2.insertVertex(Vertex(elem[0]))
        if Vertex(elem[1]) not in g2.vertex_list:
            g2.insertVertex(Vertex(elem[1]))
        g2.insertEdge(Vertex(elem[0]), Vertex(elem[1]))

    G = np.array(g1.matrix)
    P = np.array(g2.matrix)
    M = np.zeros((P.shape[0], G.shape[0]))

    M = np.zeros((P.shape[0], G.shape[1]))

    result1 = ullman(G,P,M)

    ccurrent_cols = []
    current_row = 0
    M0 = np.zeros((g2.order(), g1.order()))
    for i in range(P.shape[0]):
        p_len = np.sum(P[i, :])
        for j in range(G.shape[0]):
            g_len = np.sum(G[j, :])
            if p_len <= g_len:
                M0[i, j] = 1

    result2 = ullman_2(G,P,M0,M)
    result3 = ullman_3(G,P,M0,M)

    print(result1[0],result1[1])
    print(result2[0],result2[1])
    print(result3[0],result3[1])

