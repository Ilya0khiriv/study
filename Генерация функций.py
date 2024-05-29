
## ex 1
def math(op):
    def division(x, y):
        return x/ y

    def multiplication(x, y):
        return x * y

    def addition(x, y):
        return x + y

    def substraction(x, y):
        return x - y

    for i in [division, multiplication, addition, substraction]:
        if i.__name__ == op:
            print(f"gonna return {i.__name__} func")
            return i
    print("incorrect argument")

d = math("addition")
c = math("whaaa")
e = math("multiplication")


### ex 2
raise_to_the_power_of_two = lambda x: x ** 2
print(raise_to_the_power_of_two(12))

def raise_to_the_power_of_two_full_func(x):
    return x ** 2
print(raise_to_the_power_of_two_full_func(12))


## ex3
class Rect:

    def __init__(self,  a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

rectangle = Rect(9, 2)
print(rectangle())
