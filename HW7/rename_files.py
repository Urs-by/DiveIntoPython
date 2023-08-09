__all__ = ['group_rename']

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
from os import renames, getcwd, path, chdir, walk



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

    capacity = numb_to_capacity(count_nums)
    num = 1
    # проходимся циклом по всем вложенным дирректориям
    for cur_dir in walk(getcwd()):
        # изменяем деректорию для работы с файлами
        chdir(cur_dir[0])
        # запоминаем список файлов в директории
        list_files = cur_dir[2]

        for file in list_files:
            name_file, ext_file = path.splitext(file)
            if ext_file == extension_old:
                ext_file = extension_new
                name_file = name_file[diapazon[0] - 1:diapazon[1]] + wanted_name + str(num)
                # если количество нумерации файлов превышена , дальнейшую нумерацию прекращаем
                if capacity > 1:
                    num += 1
                    capacity -= 1
                else:
                    num = ''
                renames(file, name_file + ext_file)


if __name__ == '__main__':
    TEST_DIRECTORY = '/for_test'
    directory = getcwd() + TEST_DIRECTORY
    group_rename(wanted_name='audio', extension_old='.doc', extension_new='.mp3')
