# Compare and contrast the map() and filter() functions in Python.

""" 
Answer:
Map applies given function to every item of an iterable
to transforms each item and returns the result.

filter applies given function that returns True/False to each item
and Keeps only the elements that satisfy the condition .
"""

#example 
#map
l=["one","two","three"]
print("Original list: ",l)
nl= map(lambda i:i.upper(),l)
print( "Modified list: ",list(nl))

#filter
l=[1,2,3,4]
e=filter(lambda i:i%2==0 ,l)
print(list(e))