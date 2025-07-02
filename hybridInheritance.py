class A:
    def __init__(self):
        print("Hey chutki")
class B(A):
    def meth2(self):
        print("Hello bheem")
class C(A):
    def meth3(self):
        print("Hello kalia")
class D(B,C):
    def meth4(self):
        print("Hello Edward")

obj2=D()
obj2.meth2()
obj2.meth3()
obj2.meth4()


