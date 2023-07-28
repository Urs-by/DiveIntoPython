# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def rev_kwargs1(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        try:
            my_dict[value] = key
        except:
            my_dict[str(value)] = key
    return my_dict


# если все значение переводить в строковый тип
def rev_kwargs2(**kwargs):
    return {str(value): key for key, value in kwargs.items()}


print(rev_kwargs1(one=1, two="два", reverse=[1, 2, 3]))
print(rev_kwargs2(one=1, two="два", reverse=[1, 2, 3]))
