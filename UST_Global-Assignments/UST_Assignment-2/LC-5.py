# Can you use an if condition inside a list comprehension? 
# Provide an example where only odd numbers are selected from a list.
"""
Yes we can using if condition inside a list comprehension
"""
#example

l=[1,2,3,4,5,6,7]
nl=[i for i in l if i%2==1]
print(nl)