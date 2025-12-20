# What is the difference between a list and a tuple in Python?

"""
Answer:
The main difference between  and list is 
Tuple is immutable and list is mutable
This means Tuples cannot be modified whereas list can be modified

and the other difference is in syntax
syntax for list:
l=[1,2,3]
syntax for tuple:
t=(1,2,3)

"""
#List example
lst = [1, 2, 3, 4, 5]
lst[1:3] = [10, 20]
print(lst) 

# output of above code
# [1, 10, 20, 4, 5]


#tuple example
t=(1,2,3,4)
print("tuple before trying to modify")
try:
    t[2]=10
    print(t)
except :
    print("tuple cannot be modified")

# output of the above code
# tuple before trying to modify (1, 2, 3, 4)
# tuple cannot be modified
    
