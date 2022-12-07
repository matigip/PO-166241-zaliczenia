import sys
from pizza import Pizza


class Slice(Pizza):
    __how_many_slices: int

    def __init__(self, diameter: float, toppings: float, how_many_slices: int):
        super().__init__(diameter, toppings)
        self.toppings = None
        self.price = None
        if how_many_slices < 4 or how_many_slices > 12:
            if how_many_slices % 2 == 0:
                print("Błędna ilość kawałków")
                sys.exit(-10)
        else:
            self.__how_many_slices = how_many_slices

    @property
    def how_many_slices(self):
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, how_many_slices: int):
        if how_many_slices < 4 or how_many_slices > 12 and how_many_slices % 2 == 1:
            print('Zła ilosc kawalkow')
            sys.exit(-10)
        self.__how_many_slices = how_many_slices

    @how_many_slices.getter
    def how_many_slices(self):
        return self.__how_many_slices

    def part_price(self, ordered_slices):
        if ordered_slices > self.how_many_slices:
            raise ValueError('za duzo kawalkow chcesz')
        ile = ordered_slices / self.how_many_slices
        return self.price * ile

    def __str__(self):
        if len(self.toppings) == 0:
            return f'Pizza:\n' \
                   f'średnica: {self.diameter}\n' \
                   f'cena: {self.price}\n' \
                   f'kawałki: {self.how_many_slices}.\'' \
                   f'cena za kawałek: {self.price / self.how_many_slices}.\n'

        return f'Pizza:\n' \
               f'średnica: {self.diameter}\n' \
               f'dodatki: {self.toppings}\n' \
               f'cena: {self.price}\n' \
               f'kawałki: {self.how_many_slices}.\n' \
               f'cena za kawałek: {self.price / self.how_many_slices}.\n'
