# Класс из предыдущего урока

class MyException(Exception):
    pass


class MyExceptionAddMatrix(MyException):
    """
    Класс MyExceptionAddMatrix исключение при сложении матриц
    """

    def __init__(self, length_one, length_two, width_one, width_two):
        self.length_one = length_one
        self.width_one = width_one
        self.length_two = length_two
        self.width_two = width_two

    def __str__(self):
        return f'Длины матриц {self.length_one} и {self.length_two} должны совпадать' \
               f'  И ширины матриц {self.width_one} и {self.width_two} также должны совпадать'


class MyExceptionMultMatrix(MyException):
    """
    Класс MyExceptionMultMatrix исключение при перемножении матриц
    """

    def __init__(self, length_one, width_two):
        self.length_one = length_one
        self.width_two = width_two

    def __str__(self):
        return f'Количество столбцов 1-й матрицы: {self.length_one} должно быть равно количеству строк 2-й матрицы: {self.width_two}'


class Matrix:
    """
    Класс Матрица
    """

    def __init__(self, matrix: list):
        self.matrix = matrix
        self.len_matrix = len(matrix)
        self.width_matrix = len(matrix[0])

    def __eq__(self, other):
        """
        метод сравнение 2х матриц
        >>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 4]])
        True

        >>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 4], [5, 6]])
        False

        >>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 1], [1, 1]])
        False
        """
        if self.len_matrix != other.len_matrix or self.width_matrix != other.width_matrix:
            return False
        for i in range(self.len_matrix):
            for j in range(self.width_matrix):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        Метод сложения 2х матриц
        >>> Matrix([[1, 2], [3, 4]]) + Matrix([[1, 2], [3, 4]]) == Matrix([[2, 4], [6, 8]])
        True

        >>> Matrix([[1, 2], [3, 4]]) + Matrix([[1, 2, 5], [3, 4, 5]])
        Traceback (most recent call last):
            ...
        MyExceptionAddMatrix: Длины матриц 2 и 2 должны совпадать  И ширины матриц 2 и 3 также должны совпадать
        """
        new_matrix = [[None] * self.width_matrix for _ in range(self.len_matrix)]

        if self.len_matrix == other.len_matrix and self.width_matrix == other.width_matrix:
            for i in range(self.len_matrix):
                for j in range(self.width_matrix):
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(new_matrix)
        else:
            raise MyExceptionAddMatrix(self.len_matrix, other.len_matrix, self.width_matrix, other.width_matrix)

    def __mul__(self, other):
        '''
        Метод умножения 2х матриц
        >>> Matrix([[1, 2], [3, 4]]) * Matrix([[1, 2], [3, 4]]) == Matrix([[7, 10], [15, 22]])
        True

        >>> Matrix([[1, 2], [3, 4]]) * Matrix([[7, 8], [9, 1], [2, 3]])
        Traceback (most recent call last):
        ...
        MyExceptionMultMatrix: Количество столбцов 1-й матрицы: 2 должно быть равно количеству строк 2-й матрицы: 3
        '''

        if self.width_matrix == other.len_matrix:
            new_matrix = [[0] * other.width_matrix for _ in range(self.len_matrix)]
            for i in range(self.len_matrix):
                for j in range(other.width_matrix):
                    for k in range(self.width_matrix):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(new_matrix)
        else:
            raise MyExceptionMultMatrix(self.width_matrix, other.len_matrix)

    def __str__(self):
        return f' {self.matrix=}'

    def __repr__(self) -> str:
        return f'{self.matrix=} , {self.len_matrix=}, {self.width_matrix=}'


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    # m1 = Matrix([[1, 2], [3, 4]])
    # m2 = Matrix([[7, 8], [9, 1], [2, 3]])
    # # # m3 = Matrix([[1, 2], [3, 4]])
    # # #
    # # print(m1 + m2)
    # # #print(m1 + m3)
    # print(m1 * m2)
    # #print(m1 * m3)
