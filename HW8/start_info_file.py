from homework8 import *

file_name = 'info_file'

path_dir = os.getcwd()
res_list = (get_info_dir(path_dir))
total_list = get_info_file(path_dir, res_list)
os.chdir(path_dir)
list_to_json(file_name, total_list)
list_to_csv(file_name, total_list)
list_to_byte(file_name, total_list)
