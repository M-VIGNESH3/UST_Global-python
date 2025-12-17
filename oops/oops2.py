class Staff: 
    def __init__(self ,name,age):
        self.name=name 
        self.age=age 
    def showInfo(self):
        print("Name     " , self.name)
        print("Age      " , self.age)

s1=Staff('Doss' , 45)
s1.showInfo()
s2=Staff('Muru' , 35)
s2.showInfo()