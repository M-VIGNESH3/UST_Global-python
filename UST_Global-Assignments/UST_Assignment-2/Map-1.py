# How does the map() function work in Python? 
# Give an example where you square each number in a list.

"""
Answer:
it is a fuction that applies the given function on items in iterable
and return map obj 
"""
l=[1,2,3,4,5]
print("Original list",l)
s=map(lambda i:i**2 , l)
print("Squared list",list(s))