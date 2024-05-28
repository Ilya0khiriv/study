import math
from cprint import cprint


class Figure():
    sides_count = None
    useful_sides = None

    def __init__(self, color, *sides, filled=False):
        self.__color = None
        self.__sides = None

        self.set_color(color[0], color[1], color[2])
        self.set_sides(*sides)

        self.status()

    def status(self):
        cprint.ok(f"object {self}, color {self.__color}, sides {self.__sides}")

    def get_color(self):
        return self.__color

    def __is_valid_color(self, c1, c2, c3):
        colors = [c1, c2, c3]
        for color in colors:
            if not (0 <= color <= 255):
                return False
        return True

    def set_color(self, c1, c2, c3):
        if self.__is_valid_color(c1, c2, c3) == True: self.__color = [c1, c2, c3]

    def __is_valid_sides(self, sides):

        if len(sides) == self.useful_sides and (0 not in sides):
            return True
        return False

    def set_sides(self, *args):
        old_sides = self.__sides

        if self.__is_valid_sides(args) == True:
            self.__sides = list(args)

            if "Triangle" in str(self):
                if self.is_triangle_impossible() is True:
                    self.__sides = old_sides
                    return

            if self.useful_sides == 1:
                list_ = []
                for i in range(self.sides_count):
                    list_.append(self.__sides[0])
                self.__sides = list_
                del list_


    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self.__sides is not None:
            return sum(self.__sides)
        else:
            return 0


    def is_triangle_impossible(self):
            p = len(self) / 2

            if p == 0:
                return "Can't calculate, no sides detected"

            a, b, c = self.__sides
            v = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
            if isinstance(v, complex):
                 print("impossible triangle!")
                 return True
            return round(v, 2)


class Circle(Figure):
    sides_count = 1
    useful_sides = 1

    def __init__(self, *args):
        Figure.__init__(self, *args)
        self.__radius = None

    def get_square(self):
        print(round((len(self) ** 2) / 4 * math.pi, 2))


class Cube(Figure):
    sides_count = 12
    useful_sides = 1

    def __init__(self, *args):
        Figure.__init__(self, *args)

    def get_volume(self):
        return (len(self) // self.sides_count) ** 3


class Triangle(Figure):
    sides_count = 3
    useful_sides = 3

    def __init__(self, *args):
        Figure.__init__(self, *args)
        self__height = None

    def get_square(self):
        print(self.is_triangle_impossible())



if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    circle1.set_color(55, 66, 77)  # Изменится
    cube1.set_color(300, 70, 15)  # Не изменится

    circle1.status()
    cube1.status()

    print(circle1.get_color())
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    circle1.set_sides(15)  # Изменится

    circle1.status()
    cube1.status()

    print(cube1.get_sides())
    print(circle1.get_sides())

    print(len(circle1))

    print(cube1.get_volume())
    circle1.get_square()

    triangle1 = Triangle((0, 0, 0), 3, 3, 3)
    triangle1.get_square()
