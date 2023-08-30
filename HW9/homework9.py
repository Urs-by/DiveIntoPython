# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random
from functools import wraps


def generation_csv_file() -> None:
    """Функция генерации csv файла
    """
    data = ''
    for _ in range(1, 10):
        data_line = ''.join(str(random.randint(1, 100)) + ',' for i in range(3))
        data += data_line + '\n'
    with open('data.csv', 'w') as f:
        f.write(data)


def root_calculation(func: callable):
    """
    функция декоратор перевода значений в список
    """
    my_list = []
    def wrapper():
        # print("a -root_calculation")
        with open('data.csv', 'r') as f:
            data = csv.reader(f)
            for row in data:
                result = func(int(row[0]), int(row[1]), int(row[2]))
                my_list.append(result)
            return my_list
    return wrapper


def save_to_json(func: callable):
    """
    функция декоратор сохранения параметров в json файл
    """
    try:
        with open(f'{func.__name__}.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    def wrapper(*args, **kwargs):
        arg = str(args)
        result = str(func(*args, **kwargs))
        data.update({arg: result})

        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(data, f, indent=4)

    return wrapper




#@save_to_json
@root_calculation
@save_to_json
def quadratic_equation(*args) -> float:
    """
    функция вычисляет корни квадратного уравнения
    :param a: первый коэффициент
    :param b: второй коэффициент
    :param c: свободный член
    :return: результат
    """
    a, b, c = args
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x1, x2


if __name__ == '__main__':
    generation_csv_file()
    quadratic_equation()
