class Car:
    price = 1000000
    hp = 1000000

    def horse_powers(self, *args):
        return self.hp
    def __str__(self):
        return f"The car is {self.__class__.__name__}, it has {self.hp} horsepower, the price is {self.price}"

class Nissan(Car):
    price = 100
    def horse_powers(self, arg):
        print("I am a Nissan method!")
        self.hp = arg
        return self.hp
class Kia(Car):
    price = 1002
    def horse_powers(self, arg):
        print("I am a Kia method!")
        self.hp = arg
        return self.hp

nissan = Nissan()
nissan.horse_powers(100)
print(nissan)

kia = Kia()
kia.horse_powers(1245)
print(kia)


