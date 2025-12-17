f=open("write.txt","w")
for i in range(3):
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    f.write(name+" "+str(marks)+"\n")

f.close()