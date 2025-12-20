# How can you use list comprehension to 
# generate a list of the first 10 Fibonacci numbers?

l=[0,1]
[l.append(l[-1]+l[-2]) for i in range(5)]
print("Fibonacci using list comprehension: ",l)

