# 6- to create a binary file "Stu.dat" and enter student's rollno,name,marks till the user wants

import pickle
f=open("file handling assignment/Stu.dat","wb+")
a=input("do you want to enter data y/n:")
s=[]
while(a!='n'):
    l=[]
    roll=int(input("enter rollno-"))
    name=input("enter name-")
    marks=int(input("enter marks-"))
    l.extend([roll,name,marks])
    s.append(l)
    # l.append("\n")
    # pickle.dump(l,f)
    a=input("do you want to enter data y/n:")
pickle.dump(s,f)
f.seek(0)
data=pickle.load(f)
# print(data)
for i in data:
    print(i)
f.close()






