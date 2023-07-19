# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


def division(numerator: float, denominator: float):
    """
    функция  пытается разделить числитель и знаменатель без остатка
    :param numerator: числитель
    :param denominator: знаменатель
    :return: новые числитель и знаменатель
    """
    for i in range(2, 10):
        if numerator % i == 0 and denominator % i == 0:
            numerator = numerator / i
            denominator = denominator / i
        return numerator, denominator


def reduction(numerator: float, denominator: float):
    """
    функция сокращает дробь, используя функцию division в цикле
    :param numerator: числитель
    :param denominator: знаменатель
    :return: новые числитель и знаменатель
    """
    while True:
        new_numerator, new_denominator = division(numerator, denominator)

        if new_numerator != numerator:
            numerator = new_numerator
            denominator = new_denominator
        else:
            break
    return numerator, denominator


first_fraction = "2/8"
second_fraction = "4/5"

# расплитуем строковую дробь и выделим отдельно числитель и знаменатель
first_values = first_fraction.split('/')
second_values = second_fraction.split('/')

# перемножим числитель и знаменатель 2х дробей
mult_numerator = int(first_values[0]) * int(second_values[0])
mult_denominator = int(first_values[1]) * int(second_values[1])
print(first_fraction, '*', second_fraction, '=', mult_numerator, "/", mult_denominator)

# cократим дробь
res_numerator, res_denominator = reduction(mult_numerator, mult_denominator)
print(f'сокращенный результат:  {int(res_numerator)} / {int(res_denominator)}')

# сложим дроби
sum_numerator = int(second_values[1]) * int(first_values[0]) + int(second_values[0]) * int(first_values[1])
print(first_fraction, '+', second_fraction, '=', sum_numerator, "/", mult_denominator)

# cократим дробь
res_numerator, res_denominator = reduction(sum_numerator, mult_denominator)
print(f'сокращенный результат: {int(res_numerator)} / {int(res_denominator)}')

# проверка
a = Fraction(int(first_values[0]), int(first_values[1]))
b = Fraction(int(second_values[0]), int(second_values[1]))
print(f"проверка: умножение = {a * b}")
print(f"проверка: сложение = {a + b}")
