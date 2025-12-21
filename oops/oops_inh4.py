class A:  
    def A_bike(self):                  
        print("A bike ")  

class B(A):  
    def B_bike(self):  
        print("B bike")  

class C(B):
    def C_bike(self):  
        print("C bike")  

c=C()
c.C_bike()
c.B_bike()
c.A_bike()
 
# by default it is public Access

 