class Dog:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print("Dog's name:",self.name)
class Labrador(Dog): #Single inheritance
    def sound(self):
        print("Lab woofs")
class GuideDog(Labrador): #Multilevel inheritance
    def guide(self):
        print(self.name," guides the way")
class Friendly:
    def greet(self):
        print("Friendly")
class GoldenRetriever(Dog,Friendly):   #Multiple Inheritance
    def sound(self):
        print("GOlder Retriver barks")

lab=Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog=GuideDog("Max")
guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()

