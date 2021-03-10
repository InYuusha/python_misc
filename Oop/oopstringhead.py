def format_string(string):
    class format:
        def head(self,string):
            return str(string).title()
        
    formatter=format()

    return formatter.head(string)
    
    

h_string="hello how are you"
print("Input: "+h_string)
print("Output:"+format_string(h_string))
