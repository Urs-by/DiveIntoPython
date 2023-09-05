# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """
    Класс прямоугольник
    """

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        """Функция вычисления длины"""
        return (self.width + self.length) * 2

    def calc_square(self):
        """Функция вычисления площади"""
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length_cm=
                         (self.length + other.length),
                         width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=
                         abs(self.length - other.length),
                         width_cm=self.width)

    def __eq__(self, other):
        return self.calc_square() == other.calc_square()

    def __le__(self, other):
        return self.calc_square() <= other.calc_square()

    def __lt__(self, other):
        return self.calc_square() < other.calc_square()

    def __ge__(self, other):
        return self.calc_square() >= other.calc_square()

    def __gt__(self, other):
        return self.calc_square() > other.calc_square()


    def __str__(self):
        return f'Rectangle(length_cm={self.length}, width_cm={self.width})'

    def __repr__(self):
        return f'Rectangle(length_cm={self.length}, width_cm={self.width}, {self.calc_len()=}, {self.calc_square()=}'


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2,
                   width_cm=2)
    print(f'{r1.calc_len() = }')
    print(f'{r1.calc_square() = }')
    print('---')

    r2 = Rectangle(length_cm=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_square() = }')

    r3 = r2 + r1

    print('---')
    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_square() = }')

    print(repr(r3))
