from generation_files import create_files, sort_files
from rename_files import group_rename
from random import choice

EXTEN = ('.txt', '.doc', '.pdf', '.bin')
GENERATION = 10
TEST_DIRECTORY = 'For_test'
arg_name = 'audio'
ext_old = '.bin'
ext_new = '.txt'

for i in range(GENERATION):
    create_files(ext=choice(EXTEN), directory=TEST_DIRECTORY)
sort_files()
print("файлы созданы и отсортированы")
group_rename(wanted_name=arg_name, extension_old=ext_old, extension_new=ext_new)
print("файлы переименованы")
