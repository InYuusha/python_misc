class foo(object):
    x=0
    def __init__(self):
        print("foo constructor")
        self.x=10
    def print_number(self):
        print(self.x)
class bar(foo):
    def __init__(self):
        
       super(bar,self).__init__()
       print("Bar constructor")

b=bar()
b.print_number()

        
    
        
    
