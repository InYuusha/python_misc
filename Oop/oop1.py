class person:
    def __init__(self,name):
        self.name=name

    def say_hi(self):
        print("Hello "+self.name)

p=person("Ankush")
p.say_hi()
        
