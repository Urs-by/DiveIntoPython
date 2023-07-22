# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

my_list = [2, 2, 4,  3, 6, 7, 8, 9, 0, 0]

for i in range(len(my_list)):
    number_count = my_list.count(i)

    if number_count == 1:
        my_list.remove(i)
    else:
        for _ in range(number_count - 1):
            my_list.remove(i)


print(my_list)
