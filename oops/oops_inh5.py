class A:
    def show(self):
         print("it is from A ")

class B:
    def show(self):
         print("it is from B")

class C(B,A):                   #multiple inheritance
    def print(self):
        print("It is from  c ")

c=C()        
c.print()
c.show()
 