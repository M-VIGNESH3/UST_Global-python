# Can you modify the elements of a tuple after it has been created? Why or why not?

"""
Answer:
No we cannot modify the elements of a tuple 
because tuples are immutable in python 
and cannot be modify once created

let us understand this with a code example
"""

t=(1,2,3,4)
print("tuple before trying to modify",t)
try:
    t[2]=10
    print(t)
except :
    print("tuple cannot be modified")
    

