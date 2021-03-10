class Mybaseclass:
    def methodone(self):
        print("Parent Class")
class Mychildclass:
    def methodone(self):
        print("Child Class")

def callmethodone(obj):
    obj.methodone()

inst1=Mybaseclass()
inst2=Mychildclass()

callmethodone(inst1)
callmethodone(inst2)
