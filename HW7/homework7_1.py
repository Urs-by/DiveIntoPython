"""
Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
Пример:
rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
foto_2002.txt -> o_20video001.csv
"""
from os import renames, getcwd, listdir, path, chdir


def numb_to_capacity(count_nums: int) -> int:
    """
    функция переводит разрядность в максимальное число
    :param count_nums: разрядность
    :return: последнее число при заданной разрядности
    """
    if count_nums > 0:
        return int(count_nums * '9')
    else:
        return 0


def group_rename(wanted_name: str = '',
                 count_nums: int = 1,
                 extension_old: str = '.',
                 extension_new: str = '.',
                 diapazon: list = [3, 6]) -> None:
    directory = getcwd() + TEST_DIRECTORY
    chdir(directory)
    list_files = listdir(directory)
    capacity = numb_to_capacity(count_nums)
    num = 1
    for i in list_files:
        name_file, ext_file = path.splitext(i)
        if ext_file == extension_old:
            ext_file = extension_new
            name_file = name_file[diapazon[0] - 1:diapazon[1]] + wanted_name + str(num)

            if capacity > 1:
                num += 1
                capacity -= 1
            else:
                num = ''

            renames(i, name_file + ext_file)


if __name__ == '__main__':
    TEST_DIRECTORY = '/for_test'
    group_rename(wanted_name='audio', extension_old='.txt', extension_new='.mp3')
