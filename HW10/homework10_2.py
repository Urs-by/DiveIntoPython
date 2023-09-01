#  Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
#  которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

# Context from Function HW8/homework8.py
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.

import os
from os.path import getsize, join
import json
import csv
import pickle


class WorkWithFiles():
    """
    Класс для работы с файлами
    """

    def __init__(self, path_dir: str):
        self.path_dir = path_dir

    def size_all(self, *args) -> int:
        """
        функция подсчета размера файлов, директорий
        :param path_to_dir: путь к файлу, директории
        :return: размер в байтах
        """
        total_size = 0
        for root, dirs, files in os.walk(str(*args)):
            for file in files:
                file_path = join(root, file)
                total_size += getsize(file_path)

        return total_size

    def get_info_dir(self):
        """
        функция собирает информацию о вложенных дирикториях
        :param path_dir: путь к директории
        :return: список с информацией и размерами вложенных папок
        """
        res_list = []
        type_obj = "dir"
        for root, dir_name, file_name in os.walk(self.path_dir):
            os.chdir(root)
            dir_size = WorkWithFiles.size_all(root)
            current_dir = root.split('/')[-1:][0]
            parent = root.split('/')[-2:-1][0]
            res_list.append({"name": current_dir, "parent": parent, "type": type_obj, "size": dir_size})

        return res_list

    def get_info_file(self, *args, **kwargs) -> list:
        """
        функция собирает информацию о файлах
        :param path_dir: путь к директории
        :param res_list: список с информацией о диррикториях
        :return:
        """
        type_obj = "file"
        for root, dir_name, file_name in os.walk(self.path_dir):

            os.chdir(root)
            parent = root.split('/')[-1:][0]
            if len(file_name) > 0:
                for name in file_name:

                    file_size = getsize(join(root, name))
                    #res_list = list(args[1])
                    res_list.append({"name": name, "parent": parent, "type": type_obj, "size": file_size})
        return res_list


class ListToFile:
    """
    Класс для записи списка в файл
    """

    def __init__(self, file_name: str, list_name: list):
        self.file_name = file_name
        self.list_name = list_name

    def list_to_json(self) -> None:
        """
        функция записи списка в json
        :return:
        """
        json_name = self.file_name + ".json"
        with open(json_name, 'w') as res:
            json.dump(self.list_name, res, indent=4)

    def list_to_csv(self) -> None:
        """
        функция записи списка в csv
        :return:
        """
        with open(f'{self.file_name}.csv', 'w', newline='') as res:
            csv_write = csv.DictWriter(res, fieldnames=['name',
                                                        'parent',
                                                        'type',
                                                        'size'])
            csv_write.writeheader()
            csv_write.writerows(self.list_name)

    def list_to_byte(self) -> None:
        """
        функция записи списка в байты
        :return:
        """
        with (open(f'{self.file_name}.pickle', 'wb') as res):
            pickle.dump(self.list_name, res)


if __name__ == "__main__":
    # в path_dir текущий путь
    path_dir = os.getcwd()

    # создаем экземпляр класса для работы с файлами
    q1 = WorkWithFiles(path_dir)

    # получаем список директорий
    res_list = q1.get_info_dir()

    # получаем список всех файлов
    total_list = q1.get_info_file(path_dir, res_list)

    os.chdir(path_dir)
    name_file = "hw10"
    #  создаем экземпляр класса для записи спискв файлы
    f1 = ListToFile(name_file, total_list)
    # записываем данные в разные типы файлов
    f1.list_to_json()
    f1.list_to_byte()
    f1.list_to_csv()
