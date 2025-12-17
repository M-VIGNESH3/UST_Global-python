class Staff: 
    def __init__(self ,name,age):
        self.name=name 
        self.age=age 
# _init_(self , name , age) is constructor is executed when we create an object 
# self refers to current obeject.
s1=Staff('Doss' , 45)
print("Name    " , s1.name)
print("Age     " , s1.age)