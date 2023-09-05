# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time


class MyStr(str):
    """
    Класс Моя Строка, с возможностями str и дополнительными параметрами:
    авторство, время создания
    """

    def __new__(cls, value: str, name: str) -> object:
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time_create = time.time()
        return instance

    def __repr__(self) -> str:
        return f'MyStr({self.value =}, {self.name =}, {self.time_create =})'


if __name__ == "__main__":
    str1 = MyStr(value="Это моя строка", name='Федор')
    print(str1)
    print(repr(str1))
    print(str1.__doc__)
    # print(str1.time_create)
