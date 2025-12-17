f=open('data_append.txt', 'a') 
for i in range(2):
    name=input("Enter name  ")
    mark=input("Enter marks ")
    f.write(name+" "+mark)
    f.write("\n")
f.close()