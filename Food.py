import random


class PlantFood:
    price = 0

    def __init__(self, weight, color=None):
        self.dirty = True
        self.peel = True
        self.need_pill = True
        self.weight = weight
        self.color = color if color else self.get_default_color()

    def weight(self, weight=0):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_default_color(self):
        pass

    def get_color(self):
        return self.color

    def need_pilling(self):
        ret = True if self.need_pill and self.peel else False
        return ret

    def peel(self):
        self.peel = False

    def is_dirty(self):
        return self.dirty

    def wash(self):
        self.dirty = False

    def __repr__(self):
        return f"\nThis is {type(self).__name__}. weight: {self.get_weight()} g & color is {self.get_color()} // {self.price} rub/kg"


class Fruit(PlantFood):
    pass


class Vegetable(PlantFood):
    pass


class Cucumber(Vegetable):

    def get_default_color(self):
        return "Green"

    def need_pilling(self):
        return False


class Tomato(Vegetable):

    def get_default_color(self):
        return "Red"

    def need_pilling(self):
        return False


class Zucchini(Vegetable):

    def get_default_color(self):
        return "Dark Green"


class Eggplant(Vegetable):

    def get_default_color(self):
        return "Light Green"


class RootСrop(Vegetable):
    pass


class Potatoes(RootСrop):

    def get_default_color(self):
        return "White"


class Radish(RootСrop):

    def need_pilling(self):
        return False

    def get_default_color(self):
        return "Red"


class Carrot(RootСrop):

    def get_default_color(self):
        return "Orange"


class WashedCarrot(Carrot):

    def __init__(self, weight=0, color=None):
        super().__init__(self, weight, color)
        self.dirty = False

print(__name__)

if __name__ == "__main__":

    from py2puml.py2puml import py2puml

    # outputs the PlantUML content in the terminal
    print(''.join(py2puml('', 'py2puml.domain')))

    Carrot.price = 15.0
    Cucumber.price = 120.0
    Tomato.price = 250.0


    def weigh_all(items):
        res = 0
        for item in items:
            res += item.get_weight()
        return res


    def total_cost(items):
        res = 0
        for item in items:
            res += item.get_weight() / 1000 * item.price
        return res


    basket = []

    for i in range(5):
        basket.append(Carrot(random.randint(80, 120)))
    for i in range(3):
        basket.append(Cucumber(random.randint(200, 300)))
    for i in range(5):
        basket.append(Tomato(random.randint(80, 100)))

    print(basket)
    print("Summary:")
    print(f"Weight: {weigh_all(basket)} g")
    print(f"Cost: {total_cost(basket)} rub")
