first = 'Мама мыла раму'
second = 'Рамена мало было'
compare = map(lambda x, y: list(x) == list(y), first, second)
print(list(compare))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w") as f:
            for x in data_set: f.write(f"{x}\n")

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
with open('example.txt', "r") as f: print(f.read())

class MysticBall:
    from random import choice

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return self.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

