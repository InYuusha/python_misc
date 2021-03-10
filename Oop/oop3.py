class pet:
    number_of_legs=0
    def sleep(self):
        print("zzz")
    def count_legs(self):
            print("the number of legs "+str(self.number_of_legs))

class dogs():
    def bark(self):
        print("woof")

class horse(pet , dogs):
    def animals(self):
        print("horse are the best")
        

douche=horse()
douche.number_of_legs=4
douche.count_legs()
