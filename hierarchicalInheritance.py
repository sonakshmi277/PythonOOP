class Animal:
    def __init__(self,name):
        self.name=name
class M2(Animal):
     def __init__(self, name):
        super().__init__(name)
        print("Hey")
    
    
     

class M3(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Hiiiiiii")
        

obj=M3("Kirmara")
print(obj.name)

obj2=M2("Bheem")
print(obj2.name)