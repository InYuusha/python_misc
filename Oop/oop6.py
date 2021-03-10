class dog(object):
    def makenoise(self):
        print("Bark")
class duck(object):
    def makenoise(self):
        print("Quack")
animals=[dog(),duck()]        

for a in animals:
    a.makenoise()

