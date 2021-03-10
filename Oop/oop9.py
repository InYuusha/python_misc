class DoubleIt:

    def __init__(self):
        self.start = 1

    def __iter__(self):
        self.max = 10
        return self

    def __next__(self):
        if self.start < self.max:
            self.start *= 2
            return self.start
        else:
            raise StopIteration

obj = DoubleIt()
i = iter(obj)
print(next(i))
