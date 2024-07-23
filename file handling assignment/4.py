# 4- to count the number of words starting with "i" in a file Word.txt

f=open("file handling assignment/Word.txt","w+")
f.write("In the beginning, there was light.\nIt is a beautiful day outside.\nIce cream is a delicious treat on a hot day.\nInvest in yourself, it pays the best interest.")
f.seek(0)
data=f.readlines()
c=0
for i in data:
    for j in i.split():
        if j[0]=='i':
            c+=1
            print(j)
print("total count=",c)
f.close()