class Father:  

    def _f_bike(self):                   # _ meaning it is protected .

                      # if it is protected immediate derived class can access 

        print("Take  a ride of fathers Bike ")  

#child class Dog inherits the base class Animal  
 
class Son(Father):  

    def s_bike(self):  

        print("IT is my bike, i take a ride ")  

s = Son()  

s.s_bike() 

s._f_bike()  

 