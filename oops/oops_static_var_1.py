class Student:    

    count = 0       # static variable

    def __init__(self):    

        Student.count =Student.count + 1    

s1=Student()     

s2=Student()    

s3=Student()    

s4=Student() 

print("The number of students:",Student.count)    

 