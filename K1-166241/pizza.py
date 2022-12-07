import math
import sys
from typing import Dict


class Pizza:
    __price: float
    __toppings: Dict[str, int]
    __diameter: float

    def __init__(self, price: float, diameter: Dict[str, int], toppings: float = ''):
        self.price = price
        self.price = None
        self.toppings = None
        if diameter < 20:
            print("błędny promień")
            sys.exit(-10)
        self.__diameter = diameter

        toppings_values = toppings.values()
        for x in toppings_values:
            if x < 0 or x > 3:
                sys.exit(-20)
            self.__toppings = toppings
            self.__price = 0.05 * self.area(diameter) + len(toppings) * 2

    @staticmethod
    def area(x):
        return math.pi * (x / 2) ** 2

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, value=20):
        if self.diameter < value:
            print("błędna średnica")
            sys.exit(-10)

    def add_toppings(self, toppings: str):
        self.__toppings.append(toppings)
        self.__toppings += 1.0
        self.__price += 2.0

    def __str__(self):
        if len(self.toppings) == 0:
            return f'Pizza:\n' \
                   f'średnica: {self.diameter}' \
                   f'cena: {self.price}'

        return f'Pizza: \n' \
               f'średnica: {self.diameter}\n' \
               f'dodatki: {self.toppings}\n' \
               f'cena: {self.price}'

    def __add__(self, other: 'Pizza'):
        srednica = other.diameter
        if self.diameter > other.diameter:
            srednica = self.diameter
        list3 = []
        list3.extend(self.__toppings)
        list3.extend(other.__toppings)
        return Pizza(srednica, list3)

# x = Pizza(20,{'ser:' 2, 'szynka:' 1})
# x.diameter = 25
