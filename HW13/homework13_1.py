# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


import csv


class MyException(Exception):
    pass


class MyExceptionInstance(MyException):
    """
    Класс исключения на валидацию букв
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'В значении: "{self.value} " присутствует недопустимый символ!' \
               f' \n Допускаются только буквы, проверьте правильность ввода!'


class MyExceptionUpper(MyException):
    """"
    Класс исключения на валидацию заглавных букв
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f' Слово "{self.value} " должно начинаться с заглавной буквы!'


class MyExceptionItems(MyException):
    """
    Класс исключения на валидацию предмета
    """
    def __init__(self, name_item, name_student):
        self.name_item = name_item
        self.name_student = name_student

    def __str__(self):
        return f' У  студента {self.name_student}  нет  предмета - {self.name_item}'



class MyExceptionRange(MyException):
    """
    Класс исключения на валидацию оценки
    """
    def __init__(self, value, min_number, max_number):
        self.value = value
        self.min_number = min_number
        self.max_number = max_number

    def __str__(self):
        return f'Оценка {self.value} должна быть в диапазоне от {self.min_number} до {self.max_number}!'




class ValidationName:
    '''
    Метод для валидации имени
    '''

    def __set_name__(self, owner, name):
        self._paramname = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._paramname)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._paramname, value)

    def validate(self, value):
        if not value.isalpha():
            raise MyExceptionInstance(value)
        elif not value.istitle():
            raise MyExceptionUpper(value)


class ValidationNote:
    '''
    Метод для валидации параметров оценок
    '''

    def __init__(self, min_note, max_note):
        self.min_note = min_note
        self.max_note = max_note

    def __set_name__(self, owner, name):
        self._paramname = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._paramname)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._paramname, value)

    def validate(self, value):
        if not self.max_note >= value >= self.min_note or value < 0:
            raise MyExceptionRange(value, self.min_note,  self.max_note)


class Student:
    '''
    Класс студента
    '''
    __firs_name = ValidationName()
    __last_name = ValidationName()
    _note_item = ValidationNote(2, 5)
    _note_test = ValidationNote(0, 100)

    def subjects(self, filename: str):
        """
        метод для загрузки названия предметов из csv файла
        :return:
        """
        with open(filename, 'r', newline='') as f:
            items = csv.DictReader(f, fieldnames=['name_items', 'test'])
            dict_items = {i['name_items']: i['test'] for i in items}
            return dict_items

    def __init__(self, firs_name: str, last_name: str, age: int, group: str, filename: str):
        self.__firs_name = firs_name
        self.__last_name = last_name
        self.__full_name = firs_name + ' ' + last_name
        self.age = age
        self.group = group
        self.filename = filename
        self.items = self.subjects(filename)
        self.diary = {item: 0 for item in self.items.keys()}

    def set_note(self, name_item: str, note: int):
        '''
        Метод для записи оценки
        :param name_item: название предмета
        :param note: оценка
        :return:
        '''
        if name_item not in self.items.keys():
            raise MyExceptionItems(name_item, self.__full_name)

        if int(self.items[name_item]):
            self._note_test = note
            self.diary[name_item] = note
        else:
            self._note_item = note
            self.diary[name_item] = note

    def get_avg_note_items(self, bools: bool):
        '''
        Метод для получения среднего балла по предметам
        :param bools: Параметр для выбора тестирования=True  или предметов=False
        :return:
        '''
        list_items = [keys for keys, value in self.items.items() if int(value) == bools]
        summ = 0
        if bools:
            inform = 'тестированию'
        else:
            inform = 'предметам'
        for i in list_items:
            summ += self.diary[i]
        print(f'Средний бал по {inform} : {summ / len(list_items)}')

    def __str__(self):
        return f'{self.__full_name} {self.age}, {self.group}, {self.diary}'


if __name__ == "__main__":
    student = Student('Иван', 'Петров', 20, 'ЭМ22', 'ЭМ22.csv')
    # student1 = Student('И1ван', 'Петров', 20, 'ЭМ22', 'ЭМ22.csv')
    # student2 = Student('Иван', 'петров', 20, 'ЭМ22', 'ЭМ22.csv')

    # student.set_note('история', 40)
    student.set_note('физика', 4)
    print(student)
