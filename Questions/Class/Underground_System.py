# Leetcode 139. Design Underground System

# There is a dictionary of starting station names.
# Inside each ID of that dicitonary, there is another dictionary
# of destination stations and the value of the second dicionary is an array of count 
# (number of journeys between this starting and ending station) and value (starting t minus destination t)
# So each starting station in the first dictionary can have many destination stations
# but increment the destination count if there already has a journey between the stations


from collections import defaultdict 
class UndergroundSystem:
    def __init__(self):
        self.times = defaultdict(lambda : defaultdict(lambda : [0, 0]))
        self.transit = defaultdict(list)    # defaultdict of a list
        

    def checkIn(self, id: int, sname: str, t: int) -> None:
        self.transit[id].extend([sname, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        srcname, srct = self.transit[id]
        count, val = self.times[srcname][stationName] 
        self.times[srcname][stationName] = [count+1, val+t-srct] 
        self.transit[id] = []

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, val = self.times[startStation][endStation] 
        return val / count

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkIn(3, "Leyton", 15)
undergroundSystem.checkOut(3, "Cambridge", 50)
undergroundSystem.checkOut(32, "Cambridge", 22)
undergroundSystem.getAverageTime("Paradise", "Cambridge")


obj = UndergroundSystem()
obj.checkIn(596854,"EQH524YN",13)
obj.checkIn(29725,"Y1A2ROGU",17)
obj.checkOut(596854,"8AYN1B7O",115)
obj.checkIn(579716,"EQH524YN",145)
obj.checkOut(579716,"8AYN1B7O",199)
obj.checkOut(29725,"8AYN1B7O",295)
obj.checkIn(939079,"16MTS56Z",371)
param_3 = obj.getAverageTime("EQH524YN","8AYN1B7O")
param_3 = obj.getAverageTime("Y1A2ROGU","8AYN1B7O")
obj.checkIn(697035,"EQH524YN",442)
obj.checkIn(90668,"Y1A2ROGU",508)
param_3 = obj.getAverageTime("EQH524YN","8AYN1B7O")


# obj = UndergroundSystem()
# obj.checkIn(10,"Leyton",4)
# obj.checkIn(12,"Leyton",3)
# obj.checkOut(10,"Paradise",8)
# obj.checkOut(12,"Waterloo",12)
# obj.checkIn(5,"Leyton",10)
# obj.checkOut(5,"Waterloo",50)
# obj.checkIn(7,"Cambridge",2)
# obj.checkOut(7,"Waterloo",13)
# param_3 = obj.getAverageTime("Leyton", "Waterloo")



# print(self.end_arr[x])
# print(self.end_arr[x][0][0])

# if self.end_arr[x][0][0] == startStation:
#     print("Start station: ", self.end_arr[x][0][0])
#     print("End station: ", x)
#     print("Start time: ", self.end_arr[x][0][1])
#     print("End time: ", self.end_arr[x][1])