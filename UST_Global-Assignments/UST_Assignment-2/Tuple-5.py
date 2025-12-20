# Write a Python function that takes a tuple of numbers and returns the sum of all its elements.

def sumOfTuple(t):
    s=0
    for i in t:
        s+=i
    return s

t=(1,2,3,4,5)
print("tuple is : ",t)
print("sum of elements in tuple : ",sumOfTuple(t))