class Father:
    def __f_bike(self):  #__ will make it private

        print("Take  a ride of fathers Bike ")  

#child class Dog inherits the base class Animal  
 
class Son(Father):  

    def s_bike(self):  

        print("IT is my bike, i take a ride ")  

s = Son()  

s.__f_bike()  

s.s_bike()  
 