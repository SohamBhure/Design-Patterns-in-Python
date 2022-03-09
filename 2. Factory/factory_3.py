from abc import ABC
from enum import Enum, auto
from mimetypes import init
from pickle import FALSE, TRUE


class HotDrink(ABC):

    def consume(self):
        pass


class Tea(HotDrink):

    def consume(self):
        print('This is Tea')
        

class Coffee(HotDrink):

    def consume(self):
        print('This is Coffee')



class HotDrinkFactory(ABC):

    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):

    def prepare(self, amount):
        print('Preparing Tea')
        return Tea()

class CoffeeFactory(HotDrinkFactory):

    def prepare(self, amount):
        print('Preparing Coffee')
        return Coffee()


def make_drink(type):

    if(type == 'tea'):
        return TeaFactory().prepare(20)

    if(type == 'coffee'):
        return CoffeeFactory().prepare(20)


class HotDrinkMachine:

    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()


    factories = []
    initialize = FALSE

    def __init__(self) -> None:
        if not self.initialize:
            self.initialize = TRUE
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:0].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("\nAvailable Drinks- \nTea:0\nCoffee:1")
        for f in self.factories:
            print(f[0])

        s = input("Drink?: ")
        idx = int(s)
        s = input("Specify Amount: ")
        amount = int(s)

        return self.factories[idx][1].prepare(amount)
    



#entry = input("Which Drink?\n")
#drink = make_drink(entry)
#drink.consume()

hdm = HotDrinkMachine()
hdm.make_drink()