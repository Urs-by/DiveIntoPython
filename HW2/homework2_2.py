# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
from typing import Tuple, Any

num_dec = 1000
calculated = num_dec
HEX_DIV = 16

hex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]
res = ''
while calculated > 0:
    remainder = calculated % HEX_DIV
    res += str(hex_list[remainder - 1])
    calculated = calculated // HEX_DIV

res = res[::-1]
print(res, hex(num_dec))




