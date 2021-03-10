class Alien:
    def __init__(self):
        self.x=0
        self.y=0
    def update(self):
        self.x=self.x+5
    def draw(self):
        print("%d %d"%(self.x,self.y))


alien=Alien()
alien.update()
alien.draw()
