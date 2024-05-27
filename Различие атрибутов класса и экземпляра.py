class Building:
    total = 0
    def __init__(self):
        Building.total += 1
        self.total = Building.total


list = []
for i in range(40):
    list.append(Building())

print(list)
print(list[0].total)