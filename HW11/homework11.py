# Создайте класс Матрица.
# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.len_matrix = len(matrix)
        self.width_matrix = len(matrix[0])

    def __eq__(self, other):
        if self.len_matrix != other.len_matrix or self.width_matrix != other.width_matrix:
            return False
        for i in range(self.len_matrix):
            for j in range(self.width_matrix):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        new_matrix = [[None] * self.width_matrix for _ in range(self.len_matrix)]

        if self.len_matrix == other.len_matrix and self.width_matrix == other.width_matrix:
            for i in range(self.len_matrix):
                for j in range(self.width_matrix):
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(new_matrix)
        else:
            return ValueError('Невозможно сложить матрицы, количество строк и столбцов  матриц '
                              'должны совпадать')

    def __mul__(self, other):
        if self.width_matrix == other.len_matrix:
            new_matrix = [[0] * other.width_matrix for _ in range(self.len_matrix)]
            for i in range(self.len_matrix):
                for j in range(other.width_matrix):
                    for k in range(self.width_matrix):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(new_matrix)
        else:
            return ValueError('Невозможно перемножить матрицы, количество строк первой матрицы \n'
                              'должно равняться количеству столбцов второй матрицы')

    def __str__(self):
        return f' {self.matrix=}'

    def __repr__(self) -> str:
        return f'{self.matrix=} , {self.len_matrix=}, {self.width_matrix=}'


if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 8], [9, 1], [2, 3]])
    m3 = Matrix([[1, 2, 3], [4, 5, 6]])

    print(m1 + m2)
    print(m1 + m3)
    print(m1 * m2)
    print(m1 * m3)
