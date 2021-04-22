import random

# In python I can only use @abstractmethod and the ABC module. 
class bank():
    def __init__(self):
        self.customers = {1:{"name": "Stuart", "amount": 100}}
        
    def display_amount(self, id):
        if self.customers:
            print(self.customers[id]["name"])
            print(self.customers[id]["amount"])

class Person():
    def __init__(self, name, age):
        integer = random.randint(1,100)
        self.name = name
        self.age = age
        self.customerNumber = integer
    
    def findCustomerNumber(self):
        print(self.customerNumber)


b1 = bank()
b1.display_amount(1)
p1 = Person("Tom", 33)
p1.findCustomerNumber()
print(p1.customerNumber)
