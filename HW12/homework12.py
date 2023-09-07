# Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра.
#    Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


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
            raise ValueError(" Имя и фамилия должны содержать только буквы ")
        elif not value.istitle():
            raise ValueError(" Имя и фамилия должны начинаться с заглавной буквы")


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
            raise ValueError(f"Оценка вне диапазона от {self.min_note} до {self.max_note}")


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
            raise ValueError(f"У данного студента нет  предмета- {name_item}")

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
    student1 = Student('Иван', 'Петров', 20, 'ЭМ22', 'ЭМ22.csv')
    print(student1)
    student1.set_note('математика', 4)
    student1.set_note('история', 5)
    student1.set_note('информатика', 3)
    student1.set_note('логика', 44)
    student1.set_note('философия', 73)
    print(student1)
    student1.get_avg_note_items(True)
    student1.get_avg_note_items(False)

    student2 = Student('Ольга', 'Сидорова', 22, 'ПЭ12', 'ПЭ12.csv')
    print(student2)
    student2.set_note('физика', 3)
    student2.set_note('черчение', 4)
    student2.set_note('техника безопасности', 95)
    student2.get_avg_note_items(True)
    student2.get_avg_note_items(False)

    print(student2)
