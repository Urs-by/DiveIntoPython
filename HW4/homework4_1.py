# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def transposition1(in_matrix: list) -> list:
    res = zip(*in_matrix)
    new_matrix = [list(i) for i in res]
    return new_matrix


def transposition2(in_matrix: list) -> list:
    return [list(i) for i in (zip(*in_matrix))]


matrix = [[1, 2, 3], [7, 8, 9, ]]

print(transposition1(matrix))
print(transposition2(matrix))
