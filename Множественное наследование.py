class Vehicle:
    def __init__(self, *args):
        self.vehicle_type = "none"

class Car():
    def __init__(self, *args):
        self.price = 1000000

    def horse_powers(self):
        return 100

class Nissan(Vehicle, Car):
    def __init__(self, *args):
        Vehicle.__init__(self, *args)
        Car.__init__(self, *args)
        self.price = 121212
        self.vehicle_type = "cool type"

    def horse_powers(self):
        return 120

l = Nissan()
print(l.vehicle_type, l.price)