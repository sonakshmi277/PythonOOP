class Demo:
    def __new__(cls):
        print("Demo's __new__() invoked")
        instance = super().__new__(cls)  # properly create the object
        return instance

    def __init__(self):
        print("Demo's __init__() invoked")

class Derived_Demo(Demo):
    def __new__(cls):
        print("Derived_Demo's __new__() invoked")
        instance = super().__new__(cls)  # call Demo's __new__ and create instance
        return instance

    def __init__(self):
        print("Derived_Demo's __init__() invoked")

def main():
    obj1 = Derived_Demo()  # triggers __new__ and then __init__
    obj2 = Demo()          # triggers __new__ and then __init__

main()
