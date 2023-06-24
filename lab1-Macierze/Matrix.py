#Michał Cynarski
# skończone

class Matrix:

    def __init__(self, _matrix, par: int = 0):

        if isinstance(_matrix, tuple):
            self.__matrix = [[par] * _matrix[1] for _ in range(_matrix[0])]
        else:
            self.__matrix = _matrix

    def __str__(self):

        result = ""
        for row in self.__matrix:
            result += "| "
            for i in row:
                result += str(i) + " "
            result += "|\n"
        return result

    def __add__(self, other):

        if self.size() == other.size():

            new_matrix = Matrix([[0] * self.size()[1] for i in range(self.size()[0])])

            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    new_matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]

        else:
            raise ValueError

        return new_matrix

    def __mul__(self, other):

        if self.size()[1] == other.size()[0]:

            new_matrix = Matrix([[0] * self.size()[0] for i in range(other.size()[1])])

            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    for k in range(self.size()[1]):
                        new_matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]

        else:
            raise ValueError

        return new_matrix

    def __getitem__(self, item):
        return self.__matrix[item]

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])


def transpose(matrix: Matrix):
    transpose_matrix = Matrix([[0] * matrix.size()[0] for i in range(matrix.size()[1])])
    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix


def main():
    A = Matrix([[1, 0, 2],
                [-1, 3, 1]])
    B = Matrix((2, 3), 1)
    C = Matrix([[3, 1],
                [2, 1],
                [1, 0]])
    print(transpose(A))
    print(A + B)
    print(A * C)


if __name__ == '__main__':
    main()
