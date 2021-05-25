from enum import Enum
class VehicleSize(Enum):
    MOTORCYCLE = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4

class Vehicle:
    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_taken = []

class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        self.time = 1
        super(Motorcycle, self).__init__(VehicleSize.MOTORCYCLE, license_plate, spot_size=1)


aa = Motorcycle("aaaa")


# ENUM methods
class colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(repr(colour.RED))
print(colour.RED.name)
print(colour.RED.value)
for i in colour:
    print(i.value)