from enum import Enum
class Category(Enum):
    SIMPLE_VEG = 2.0,
    CLASSIC_VEG = 2.5,
    EXOTIC_VEG = 3.0

class Pizza:
    def __init__(self, pizza, crust = "Pan", top1 = None, top2 = None):
        self.pizza = pizza
        self.crust = crust
        self.top1 = top1
        self.top2 = top2
        self.price = 0.0
        self.toppings = {
            "Tomato" : 0.1,
            "Jalapeno" : 0.1,
            "Olives" : 0.2,
            "Paneer" : 0.2,
            "Capsicum" : 0.1,
            "Corn" : 0.1,
            "Cheese" : 0.3
        }
        self.crusts = {
            "Pan" : 0.0,
            "Thin" : 0.4,
            "Cheese Burst" : 0.8
        }

        self.categories = {
            "Margherita" : Category.SIMPLE_VEG,
            "Cheese n'Tomato" : Category.SIMPLE_VEG,
            "Farmhouse" : Category.CLASSIC_VEG,
            "Veg Supreme": Category.CLASSIC_VEG,
            "Mexican Green Wave" : Category.EXOTIC_VEG,
            "Peppy Paneer" : Category.EXOTIC_VEG
        }
        self.validate_crust()
        self.validate_pizza()
        self.validate_toppings()


    def validate_toppings(self):
        if self.top1 or self.top2:
            if self.top1 in self.toppings:
                try:
                    self.price += self.toppings[self.top1]
                except KeyError:
                    return "Topping not found"
            if self.top2 in self.toppings:
                try:
                    self.price += self.toppings[self.top2]
                except KeyError:
                    return "Topping not found"
        else:
            return "Toppings required"

    def validate_crust(self):
        try:
            self.price += self.crusts[self.crust]
        except KeyError:
            return "Crust not found"

    def validate_pizza(self):
        try:
            aa = self.categories[self.pizza]
            self.price += aa.value
        except KeyError:
            return "Pizza not valid"


obj_1 = Pizza("Mexican Green Wave", "Cheese Burst", "Olives", "Corn")
# obj_1.validate_toppings()
# obj_1.validate_crust()
# obj_1.validate_pizza()
print(obj_1.price)



