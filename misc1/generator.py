def sample():
    yield 1
    yield 2
    yield 3
x=sample()
print(x.__next__())
    
