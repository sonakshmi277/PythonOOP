class Dog:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if(age>0):
            self.__age=age
        else:
            print("Invalid age")
    def __bark(self):
        print(f"{self.name} barks: Woof Woof!")

    # ---------- Public wrapper that calls private method ----------
    def show_behavior(self):
        print(f"{self.name} is {self.__age} years old.")
        self.__bark()
dog = Dog("Buddy", 3)

# Working with private attribute
print(dog.get_age())   # ✅ getter
dog.set_age(5)         # ✅ setter
print(dog.get_age())
dog.show_behavior()    # ✅ prints name, age, and calls __bark
