class father:
    def __init__(self,param):
        self.o1=param

class child(father):
    def __init__(self,param):
        self.o2=param
        super().__init__(67)

obj=child(22)
print("%d %d" %(obj.o1,obj.o2))

