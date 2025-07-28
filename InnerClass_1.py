class Student:
    def __init__(self,name):
        self.name=name
        self.laptop=self.Laptop()
    def show(self):
        print(f"name:{self.name}")
        self.laptop.show()
    class Laptop:
        def __init__(self):
            self.brand="brand"
        def show(self):
            print(f"Laptop:{self.brand}")
obj=Student("Sonakshmi")
obj.show()    

