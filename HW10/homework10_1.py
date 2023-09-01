# Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from seminar10_5 import Dog, Fish, Kotopes


class Factory():

    def __init__(self, type_animal: str, *args, **kwargs) -> None:
        self.type_animal = type_animal
        self.args = args
        self.kwargs = kwargs

    def create_new_animal(self, *args, **kwargs):
        type_animals = ["fish", "dog", "kotopes"]
        if self.type_animal in type_animals:
            if self.type_animal == "dog":

                new_animal = Dog(*self.args, **self.kwargs)
            elif self.type_animal == "fish":
                new_animal = Fish(*self.args, **self.kwargs)

            elif self.type_animal == "kotopes":
                new_animal = Kotopes(*self.args, **self.kwargs)
            else:
                new_animal = None

        return new_animal


if __name__ == "__main__":
    new_animal1 = Factory('kotopes', 3, "черте-что", 2)
    new_animal2 = Factory('dog', 'Тузик', 4, "серый", "спаниель", False)
    new_animal3 = Factory('fish', "Nemo", 1, True, 0.5)

    himera = new_animal1.create_new_animal()
    tuzik = new_animal2.create_new_animal()
    nemo = new_animal3.create_new_animal()
    print(himera)
    print(tuzik)
    print(nemo)
    # dory = new_animal.create_new_animal()
