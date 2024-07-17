class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, hp):
        self.owner = owner
        self.__model = model
        self.__engine_power = hp
        self.__color = color

    def get_model(self):
        print(f"Model: {self.__model}")

    def get_horsepower(self):
        print(f"Horsepowers: {self.__engine_power}")

    def get_color(self):
        print(f"Color: {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Owner: {self.owner}")

    def set_color(self, new_color):
        for _one_color in self.__COLOR_VARIANTS:
            if _one_color.lower() == new_color.lower():
                self.__color = new_color
                return
        print(f"Can't change color to {new_color}")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
