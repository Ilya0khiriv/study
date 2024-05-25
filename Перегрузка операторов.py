

class Building():

    def __init__(self, floors = 0, type = 0):
        self.numberOfFloors = floors
        self.buildingType = type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


e = Building(floors=1, type=9)
c = Building(floors=1, type=2)

print(c == e)
