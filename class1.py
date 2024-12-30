class newclass:
    n=7
    def __init__(self,name):
        self.name=name
        print("new")
    def print1(self):
        print(self.name)

obj=newclass("indhu")
print(obj.n)
obj.print()
obj1=newclass("swathi")
print(obj1.n)
obj1.n=23
print(obj,obj1.n)

'''
class example_class():
    def method_1(self):
        print("Example Class method_1")
        
    def method_2(self,some_string):
        print("Example Class method_2 " + some_string)        

def main():
    # using class methods
    obj = example_class()
    obj.method_1()
    obj.method_2("I am passing some string")
    
    
if __name__ == "__main__": main()  

        
'''
