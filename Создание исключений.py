

class InvalideNumber(Exception):
    def __init__(self, name, extra_info):
        self.name = name
        self.extra_info = extra_info

class NotANumber(Exception):
    def __init__(self, name, extra_info):
        self.name = name
        self.extra_info = extra_info


class InvalidPerimetr(Exception):
    def __init__(self, name, extra_info):
        self.name = name
        self.extra_info = extra_info

def calculate_triangle_perimetr(a, b, c):

    def calculate_perim(p, a, b ,c):
        v = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

        if v == 0:
            raise InvalidPerimetr("Incompatible sides! Perimetr cannot be zero", v)

        if str(v)[-2] == "j":
            raise InvalidPerimetr("Incompatible sides! Perimetr cannot be a complex number", v)

        return v

    if None in (a, b, c):
        print("not all are there")



    for i in (a, b, c):

        if type(i) is not (int or float):
            raise NotANumber("A side must be a number", (a, b, c))

        if i <= 0:
            raise InvalideNumber("Cannot assign negative numbers or zero as a side", (a, b, c))

    p = (a + b + c) / 2

    try:
         v = calculate_perim(p, a, b ,c)
    except InvalidPerimetr as exc:
        return str(exc.name) + " " + str(exc.extra_info)
    return round(v, 3)

try:
    result_ = calculate_triangle_perimetr(3, 2, 4)
    print(result_)
except NotANumber as exc:
    print(exc.name, exc.extra_info)

except InvalideNumber as exc:
    print(exc.name, exc.extra_info)

