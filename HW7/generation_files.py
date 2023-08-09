__all__ = ['create_files', 'sort_files']

from random import randint, choice
from os import getcwd, mkdir, listdir, chdir
from pathlib import Path


def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_files(ext: str, directory: str = None, min_len: int = 6,
                 max_len: int = 30, min_size: int = 256,
                 max_size: int = 4096, count_files: int = 5):
    if not directory:
        directory = getcwd() + '/'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '/' + directory + '/'
    for _ in range(count_files):
        with(open(directory + give_name() + ext, 'w', encoding='utf-8') as file_output):
            list_of_bytes = bytes([randint(0, 255) for x in range(min_size, max_size)])

            file_output.write(str(list_of_bytes))

def sort_files(directory: str | Path = 'for_test'):
    chdir(directory)
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        ext = file.name.split('.')[1]
        if ext.upper() not in listdir():
            mkdir(ext.upper())
        file.replace(f"{ext.upper()}/{file.name}")



if __name__ == '__main__':
    EXTEN = ('.txt', '.doc', '.pdf', '.bin')
    create_files(ext=choice(EXTEN), directory='for_test')
    sort_files()