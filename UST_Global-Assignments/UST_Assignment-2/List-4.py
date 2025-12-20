# How can you check if an element exists in a list in 

l=[1,2,3,4,5]
el=int(input("enter the number to check if it exists in list : "))
if el in l:
    print("number exist in the list at index",l.index(el))
else:
    print("number does not exist in the list")