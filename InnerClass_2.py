class Student:
    def __init__(self,name,laptop):
        self.name=name
        self.laptop=laptop
    class Laptop:
        def __init__(self,brand):
            self.brand=brand
        def show(self):
            print(f"Brand:{self.brand}")
custom_laptop=Student.Laptop("HP")
s1=Student("Sonakshmi",custom_laptop)
s1.laptop.show()