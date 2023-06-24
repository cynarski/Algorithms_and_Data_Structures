# Michał Cynarski
# skończone

class Matrix:

    def __init__(self, _matrix, par: int = 0):

        if isinstance(_matrix, tuple):
            self.__matrix = [[par] * _matrix[1] for i in range(_matrix[0])]
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

    def __setitem__(self, key, value):
        self.__matrix[key] = value

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])


def transpose(matrix: Matrix):
    transpose_matrix = Matrix([[0] * matrix.size()[0] for _ in range(matrix.size()[1])])
    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix


def chio_det(matrix: Matrix, par=1):

    if matrix.size() == (2, 2):
        return par * (matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1])

    if matrix[0][0] == 0:
        for i in range(matrix.size()[0] + 1):
            if matrix[i][0] != 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]

                par = par * (-1)
                break

    new_par = par * 1 / (matrix[0][0] ** (matrix.size()[0] - 2))
    smaller_matrix = []

    for i in range(matrix.size()[1] - 1):

        lst = []
        for j in range(matrix.size()[1] - 1):
            lst.append(matrix[0][0] * matrix[i + 1][j + 1] - matrix[0][j + 1] * matrix[i + 1][0])
        smaller_matrix.append(lst)
    return chio_det(Matrix(smaller_matrix), new_par)


def main():
    
    A = Matrix([[5, 1, 1, 2, 3],
                [4, 2, 1, 7, 3],
                [2, 1, 2, 4, 7],
                [9, 1, 0, 7, 0],
                [1, 4, 7, 2, 2]])
    
    B = Matrix([[0, 1, 1, 2, 3],
                [4, 2, 1, 7, 3],
                [2, 1, 2, 4, 7],
                [9, 1, 0, 7, 0],
                [1, 4, 7, 2, 2]])

    print(int(chio_det(A)))
    print(int(chio_det(B)))


if __name__ == '__main__':
    main()
