class Person:
    def __init__(self,name):
        self.name=name
    def set_name(self,new_name):
        self.name=new_name
p=Person("Ria")
print(p.name)
p.set_name("Mahir")
print(p.name)
