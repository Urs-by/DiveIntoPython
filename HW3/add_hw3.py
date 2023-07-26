# Дополнительное:
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.
import copy

item_dict = {'Вася': {'рюкзак', 'палатка', 'котелок', 'фонарик'},
             'Коля': {'рюкзак', 'палатка', 'фонарик', 'спички'},
             'Миша': {'рюкзак', 'палатка', 'спички', 'велосипед'}}


def crossing(item_dict: dict) -> set:
    """
    функция пересечения возвращает какие одинаковые вещи у всех друзей
    :param item_dict: словарь со списком вещей
    :return: множество схожих вещей
    """
    res = set()
    for key in item_dict:
        if not res:  # если res пустой
            res = item_dict[key]
        else:
            res &= item_dict[key]  # выполняем операцию пересечения
    return res


def unicum(friend: str, n_dict: dict) -> dict:
    """
    функция возвращает имя друга и его вещи, которые есть только у него
    :param friend: имя друга
    :param n_dict: словарь со списком вещей
    :return: имя друга и его вещи
    """
    res = n_dict[friend]
    for key in n_dict:
        if key != friend:
            res -= n_dict[key]  # выполняем операцию удаления
    answer = {friend: res}
    return answer


def total(item_dict: dict) -> set:
    """
    функция  объединения возвращает какие одинаковые вещи у всех друзей
    :param item_dict: словарь со списком вещей
    :return: множество схожих вещей
    """
    res = set()
    for key in item_dict:
        if not res:  # если res пустой
            res = item_dict[key]
        else:
            res |= item_dict[key]  # выполняем операцию объединения
    return res


def without(friend: str, n_dict: dict) -> dict:
    """
    функция возвращает вещи которых нет у друга
    :param friend: имя друга
    :param n_dict: словарь со списком вещей
    :return: Имя друга и вещи, которых у него нет
    """
    faser_dict = copy.deepcopy(item_dict)
    res = total(faser_dict)
    res -= n_dict[friend]  # выполняем операцию вычитания
    answer = {friend: res}
    return answer



new1_dict = copy.deepcopy(item_dict)
print(f"Вещи, которые одновременно взяли все друзья: {crossing(new1_dict)}")

print("Уникальные вещи, которые взял каждый друг:")
for i in item_dict:
    new_dict = copy.deepcopy(item_dict)
    print(unicum(i, new_dict))

print("Вещи, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:")
for i in item_dict:
    new_dict = copy.deepcopy(item_dict)
    print(without(i, new_dict))


