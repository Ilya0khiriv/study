class Building:
    total = 0
    def __init__(self):
        self.total = Building.total
        Building.total += 1

for i in range(40):
    print(Building().total)