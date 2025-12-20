# How does a set handle duplicate values when adding them?

""" 
Answer:
Set only stores unique elements.
trying to add an element that already present in set,nothing changes
there will no affect on the set
and program will run withut any error
"""

s={1,2,3,4,5}
print("set before add a duplite element",s)
s.add(3)
print("set after add a duplite element",s)
