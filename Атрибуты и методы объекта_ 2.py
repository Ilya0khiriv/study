
class House():

    def __init__(self, name = None, num_of_floors = None):
        self.name = name
        self.numberOfFloors = num_of_floors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"The house has been rebuilt. Now it has {self.numberOfFloors} floors")

    def go_to(self, new_floor):
        if 0 < new_floor <= self.numberOfFloors: print(f"Floor number {new_floor}")
        else: print(f"Floor number {new_floor} doesn't exist")


home = House(name = "ЖК Эльбрус", num_of_floors = 30)
home.go_to(3)
home.setNewNumberOfFloors(7)


