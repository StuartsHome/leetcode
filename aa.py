
from enum import Enum
class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:
    def __init__(self, licence_plate, vehicle_size):
        self.licence_plate = licence_plate
        self.vehicle_size = vehicle_size

class Car(Vehicle):
    def __init__(self, licence_plate):
        super().__init__(licence_plate, VehicleSize.MEDIUM)


class ParkingLot:
    def __init__(self, available_spots):
        self.available_spots = available_spots

    def park_vehicle(self, vehicle):
        temp = self.findSpot(vehicle)

        if temp is None:
            return None
        else:
            Spot.park_vehicle



    def findSpot(self, vehicle):
        """find available spot where vehicle can fit or return none""" 
    
class Spot:
    def __init__(self, spot_number, spot_size, available):
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.available = available
        self.vehicle = None

    def park_vehicle(self, vehicle):
        pass
    def is_available(self):
        if self.vehicle:
            return False
        return True


Toyota = Car("TTT")
print(Toyota.vehicle_size)


