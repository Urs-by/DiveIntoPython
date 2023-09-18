# Вам нужно разработать скрипт, который будет считывать содержимое CSV-файла
# и категоризировать каждое письмо в соответствии с его содержимым.
# Категория должна быть определена на основе ключевых слов, содержащихся в тексте письма.
# Проанализируйте содержимое и выявите зависимости.
# Создайте словарь с ключевыми словами для каждой категории.
# Скрипт должен открывать CSV-файл, считывать каждое письмо и проверять
# его содержимое на наличие ключевых слов для каждой категории.
# Письмо должно быть отнесено к одной или нескольким категориям,
# если оно содержит соответствующие ключевые слова и корни к ним.
# Результаты категоризации должны быть сохранены в новом CSV-файле или выведены на экран в удобочитаемом формате.
# Обратите внимание, что ключевые слова могут быть регистронезависимыми,
# то есть их наличие в письме должно быть определено без учета регистра.
# Дополнительным плюсом будет реализация обработки исключений,
# чтобы скрипт не завершался с ошибкой при некорректной структуре CSV-файла или отсутствии файла.
# нужно добавить логирование несортированых сообщения и запуск из терминала.

import csv
import logging

FORMAT = \
    '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    ' записала сообщение: {msg}'

logging.basicConfig(format=FORMAT,
                    style='{',
                    filename="requests.log",
                    filemode='a',
                    encoding='utf-8',
                    level=logging.ERROR)

logger = logging.getLogger(__name__)

Security = ['безопасност', 'парол']
Refunds = ['возврат', 'верн', 'отказ', 'отмен', 'отключить', 'отписаться']
Troubleshooting = ['проблем', 'восстанов', 'глючит', 'сбой', 'разобрать', 'улучшит', 'исправ', 'ничего',
                   'почин', 'ошиб', 'подсказать', 'медленно', 'когда', 'программа', 'вопрос', 'нужно']
Account = ['аккаунт', 'авториз', 'учетн']
Advertising = ['реклам', 'размещен']
Collaboration = ['сотруднич', 'партнерство']
Limits = ['ограничен', 'лимит', 'макс', 'увелич']
Payments = ['рассрочк', 'платеж', 'оплат', 'списани', 'деньги', 'ethereum', 'mastercard',
            'pay', 'visa', 'webmoney', 'yandex.money']
Features = ['функц', 'сервис', 'подписка', 'api']

list_requests = {'Security': Security, 'Refunds': Refunds, 'Troubleshooting': Troubleshooting, 'Account': Account,
                 'Advertising': Advertising, 'Collaboration': Collaboration, 'Limits': Limits, 'Payments': Payments,
                 'Features': Features}

name_in_file = 'user_support_letters.csv'
name_out_file = 'user_sorted_letters.csv'


def read_file(name_file: str) -> list:
    '''
    функция чтения файла
    :param name_file: название файла
    :return: список с данными
    '''
    try:
        with open(name_file, 'r', newline='') as f:
            file = csv.reader(f)
            csv_file = [i for i in file]
            return csv_file
    except FileNotFoundError as error:
        logger.error(f"Файла с именем {name_file} не существует! Ошибка: {error}")
        print(f"Файла с именем {name_file} не существует! Ошибка: {error}")


def write_file(name_file: str, *args):
    '''
    функция дозаписи данных в файл
    :param name_file: имя файла
    :param args: данные для записи
    :return:
    '''
    try:
        with open(name_file, 'a', newline='', encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter=",", lineterminator="\r")
            file_writer.writerow(*args)
    except PermissionError as error:
        logger.error(f" Отказано в доступе ! Ошибка: {error}")
        print(f" Отказано в доступе ! Ошибка: {error}")


def clear_file(name_file: str):
    '''
    функция очистки файла
    :param name_file: имя файла
    :return:
    '''
    try:
        f = open(name_file, 'w')
        f.close()
    except PermissionError as error:
        logger.error(f" Отказано в доступе ! Ошибка: {error}")
        print(f" Отказано в доступе ! Ошибка: {error}")


def all_words(csv_file: list) -> dict:
    '''
    промежуточная функция для подсчета количества всех используемых слов
    для составления ключевых однокорееных слов
    :param csv_file: список обращений
    :return: частотный словарь
    '''
    words = {}
    for i in csv_file:
        requst = i[0].split()
        for j in requst:
            if j in words:
                words[j] += 1
            else:
                words[j] = 1
    return words


def search_word(word: str, list_name: list) -> bool:
    """
    функция прооверки слова в списке ключевых слов
    :param word: слово из обращения
    :param list_name: список ключевых слов
    :return: bool
    >>> search_word('пароль',['безопасност', 'парол'])
    True
    """
    try:
        for i in list_name:
            if i in word:
                return True
        return False
    except IndexError or TypeError as error:
        logger.error(f"Неожиданная ошибка! Ошибка: {error}")


def unprocessed_requests(list_request: list) -> None:
    '''
    промежуточная функция, которая выводит не обработанные запросы
    :param list_request: список обработанных запросов
    :return: список необработанных запросов
    '''
    try:
        join_list_request = [' '.join(i) for i in list_request]
        # full_list = map(str, csv_file)
        for i in csv_file:
            if i[0] not in join_list_request:
                print(i[0])
    except TypeError as error:
        logger.error(f"Неожиданная ошибка, вероятно из-за отсутствия исходного файла: {error}")


def create_list_requests(name_list: list) -> list:
    """
    фyкция, которая формирует список обращений по нужной категории
    :param name_list: список с ключевыми словами поиска
    :return: список обращений
    """
    list_request = []
    try:
        for i in csv_file:
            request = i[0].split()
            for j in request:
                if search_word(j.lower(), name_list):
                    list_request.append(request)
                    # print(request)
                    break
        return list_request
    except TypeError as error:
        logger.error(f"Неожиданная ошибка, вероятно из-за отсутствия исходного файла: {error}")
        # print(error)


def save_category_to_file() -> list:
    '''
    функция записи в новый сым файл отсортированных данных
    :return: отcортированный список обращений по категориям
    '''
    try:
        new_list_request = []
        for key, value in list_requests.items():
            i_list = create_list_requests(value)
            for j in i_list:
                if j not in new_list_request:
                    new_list_request.append(j)
                    str_j = ' '.join(j)
                    write_file(name_out_file, [key, str_j])
        return new_list_request
    except TypeError as error:
        logger.error(f"Неожиданная ошибка, вероятно из-за отсутствия исходного файла: {error}")


# вывод частотного словар
# words = all_words(csv_file)
# for key, value in sorted(words.items()):
#     print(key, value)

if __name__ == '__main__':
    csv_file = read_file(name_in_file)
    # print(len(csv_file))
    clear_file(name_out_file)
    new_list_request = save_category_to_file()
    unprocessed_requests(new_list_request)
    # print(len(new_list_request))
