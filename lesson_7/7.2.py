from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        # Расход ткани
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def expense(self):
        return round(self.param / 6.5 + 0.5)


class Jacket(Clothes):

    @property
    def expense(self):
        return round(self.param * 2 + 0.3)


a = Coat(34)
b = Jacket(20)
print(a)
print(a.expense)
print(b.expense)