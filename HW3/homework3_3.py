# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools

backpack = {"cпальный мешок": 2.5,
            "фонарь": 0.35,
            "генератор": 2.1,
            "топорик": 1.0,
            "тушонка": 1.3,
            "вода": 2.0,
            "крупа": 1.0,
            "одежда": 1.8,
            "котелок": 0.8
            }

CARRRYING = 8.0
max_sum = 0

result = []
for r in range(1, len(backpack) + 1):
    for combination in itertools.combinations(backpack.keys(), r):
        weight = 0
        for j in combination:
            weight = weight + backpack[j]
        if weight <= CARRRYING:
            print(combination, weight)

