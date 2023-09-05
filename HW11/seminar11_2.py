# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archiv:
    """
    класс Архив, который хранит пару свойств: число и строку.
    При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков-архивов
    list-архивы также являются свойствами экземпляра
    """
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, number: int) -> None:
        self.text = text
        self.number = number

    def __repr__(self) -> str:
        return f'Archiv({self.text =}, {self.number =}, {self.old_text =}, {self.old_int =})'

    def __str__(self):
        return f'Archiv {self.text} {self.number}'


if __name__ == "__main__":
    a1 = Archiv(text='T', number=1)
    a2 = Archiv(text='E', number=2)
    a3 = Archiv(text='Z',

                number=3)

    print(a2.instance.old_text)
    print(a2.instance.old_int)

    print('---')

    print(a3)
    print(repr(a3))
    print(f'{a3=}')
    print(a3.__doc__)
