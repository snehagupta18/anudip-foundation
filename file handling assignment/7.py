# 7-read binary file "Stu.dat" and print those students who have marks>81
import pickle
f=open("file handling assignment/Stu.dat","rb")
data=pickle.load(f)
for i in data:
    if i[2]>81:
        print(i)
f.close()