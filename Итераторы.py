class EvenNumbers:


    def __init__(self, start=0, end=1):
        self.count = 0
        self.start = start
        self.end = end

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        self.count += 1

        if self.start + self.count <= self.end:
            if ((self.start + self.count)% 2) == 0:
                return self.start + self.count
            else:
                self.count += 1
                return self.start + self.count

        raise StopIteration()




en = EvenNumbers(10, 25)
for i in en:
    print(i)


