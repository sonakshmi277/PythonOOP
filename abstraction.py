from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def v(self):
        pass
class B(A):
    def v(self):
        print("KIM")

w=B()
w.v()