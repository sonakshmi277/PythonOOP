class A:
    def __init__(self, x):
        self.x = x
        print("A's __init__ called")

    def __repr__(self):
        return f"A(x={self.x})"

class B(A):
    def __init__(self, x, y):
        super().__init__(x)   # call A's __init__
        self.y = y
        print("B's __init__ called")

    def __repr__(self):
        return f"{super().__repr__()}, B(y={self.y})"

class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # call B's __init__, which calls A's
        self.z = z
        print("C's __init__ called")

    def __repr__(self):
        return f"{super().__repr__()}, C(z={self.z})"

def main():
    c = C(1, 2, 3)
    print(c)
    
main()
