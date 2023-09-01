# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import os
from os.path import getsize, join
import json
import csv
import pickle


def size_all(path_to_dir: str) -> int:
    """
    функция подсчета размера файлов, директорий
    :param path_to_dir: путь к файлу, директории
    :return: размер в байтах
    """
    total_size = 0

    for root, dirs, files in os.walk(path_to_dir):
        for file in files:
            file_path = join(root, file)
            total_size += getsize(file_path)

    return total_size


def get_info_dir(path_dir: str) -> list:
    """
    функция собирает информацию о вложенных дирикториях
    :param path_dir: путь к директории
    :return: список с информацией и размерами вложенных папок
    """
    res_list = []
    type_obj = "dir"
    for root, dir_name, file_name in os.walk(path_dir):
        os.chdir(root)
        dir_size = size_all(root)
        current_dir = root.split('/')[-1:][0]
        parent = root.split('/')[-2:-1][0]
        res_list.append({"name": current_dir, "parent": parent, "type": type_obj, "size": dir_size})
    return res_list


def get_info_file(path_dir: str, res_list: list) -> list:
    """
    функция собирает информацию о файлах
    :param path_dir: путь к директории
    :param res_list: список с информацией о диррикториях
    :return:
    """
    type_obj = "file"
    for root, dir_name, file_name in os.walk(path_dir):
        os.chdir(root)
        parent = root.split('/')[-1:][0]
        if len(file_name) > 0:
            for name in file_name:
                file_size = getsize(join(root, name))
                res_list.append({"name": name, "parent": parent, "type": type_obj, "size": file_size})
    return res_list


def list_to_json(filename, info_list) -> None:
    filename += ".json"
    with open(filename, 'w') as res:
        json.dump(info_list, res, indent=4)


def list_to_byte(filename, info_list) -> None:
    with (open(f'{filename}.pickle', 'wb') as res):
        pickle.dump(info_list, res)


def list_to_csv(filename, info_list) -> None:
    print(info_list)
    with open(f'{filename}.csv', 'w', newline='') as res:
        csv_write = csv.DictWriter(res, fieldnames=['name',
                                                    'parent',
                                                    'type',
                                                    'size'])
        csv_write.writeheader()
        csv_write.writerows(info_list)


if __name__ == "__main__":
    path_dir = os.getcwd()
    res_list = (get_info_dir(path_dir))
    total_list = get_info_file(path_dir, res_list)
    print(total_list)
    os.chdir(path_dir)
    list_to_json('info_file', total_list)
    list_to_csv('info_file', total_list)
    list_to_byte('info_file', total_list)
