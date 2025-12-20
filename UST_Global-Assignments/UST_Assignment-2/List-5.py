# Write a Python function that removes duplicates from a list without using the set() function.

def remove_duplicates(lt):
    rel=[]
    for i in lt:
        if i in rel:
            continue
        else:
            rel.append(i)

    return rel



l=[1,2,2,3,3,3,4,3,5,7]
print("List before removing duplicate elements",l)
rl=remove_duplicates(l)
print("List after removing duplicate elements",rl)

