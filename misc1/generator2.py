class DoubleIt:

    def __init__(self, max=10):
        self.start = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.max:
            self.start *= 2
            return self.start
        else:
            raise StopIteration

i = iter(DoubleIt(max=16))
#print(next(i))
# 2
print(list(i))
