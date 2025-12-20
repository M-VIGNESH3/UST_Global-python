# Write a Python function that takes a dictionary and 
# returns a list of keys that have values greater than 50.

def fun(d):
    l=[]
    for k ,v in d.items():
        if v>50:
            l.append(k)
    return l


d={1:10,2:20,3:30 ,5:50,6:60,7:70}
print("dictionary is: ",d)
print("keys that have values greater than 50 is:",fun(d))
