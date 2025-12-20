# Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?
t=(1,2,3,4)
print("tuple before changing value:",t)
t=list(t)
t[2]=100
t=tuple(t)
print("tuple after changing value:",t)
