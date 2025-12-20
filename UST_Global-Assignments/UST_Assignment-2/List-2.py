# How can you remove an element from a list by its index?

l=[1,2,3,4,5]
print("List before removing any element",l)
i=int(input("enter the index to remove that element form the list: "))

if i>=len(l):
    print("Index  is out of range")
else:
    l.remove(l[i])
    print("List after removing the index element",l)
