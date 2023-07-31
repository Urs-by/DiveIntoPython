# Создайте функцию генератор чисел Фибоначчи

def generation(num: int):
    yield 1
    prev, curr = 0, 1

    for i in range(0, num):
        res = prev + curr
        prev, curr = curr, res

        yield res


print(*generation(10))
