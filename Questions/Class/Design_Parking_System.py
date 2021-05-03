# Leetcode 1603. Design Parking System

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.memo = {1: big, 2: medium, 3:small}

    def addCar(self, carType: int) -> bool:
        curr = self.memo
        if curr[carType] > 0:
            curr[carType] -= 1
            return True
        else:
            return False

["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]