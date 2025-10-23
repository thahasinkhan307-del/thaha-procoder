class emp:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
class empchild(emp):
    def __init__(self,name,age,sal,idno):
        self.name=name
        self.age=age
        self.sal=sal
        self.idno=idno

#drive code
e=emp("srikanth",23,3000)
print(" name=",e.name)
e1=empchild('iot-B',23,3000,22)
print(e1.name)
        
