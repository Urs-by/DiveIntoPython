# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def path_tuple(path_to_file: str) -> tuple:
    *start, end = path_to_file.split('/')
    path_to = '/'.join(start)
    name, extension = end.split('.')
    return path_to, name, extension


path = "/Users/arturkaratkevich/PycharmProjects/DiveIntoPython/HW5/homework5_1.py"
print(path_tuple(path))
