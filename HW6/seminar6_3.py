__all__ = ['valid_day']

from sys import argv


# проверка на високосность


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# проверка существования дня


def valid_day(date: str) -> bool:
    try:
        day, month, year = map(int, date.split('.'))
        if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
            days_in_month = [
                31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return day <= days_in_month[month - 1]
        else:
            return False
    except ValueError:
        return False


if __name__ == '__main__':
    arguments = argv[1:]


    print(valid_day(*arguments))
    input_date = input("Введите дату : ")
    print(valid_day(input_date))
    # print(valid_day('31.11.2023'))
