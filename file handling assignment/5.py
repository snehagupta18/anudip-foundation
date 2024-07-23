# 5- to display the lines having more than 5 words in a text file Notes.txt

f=open("file handling assignment/Notes.txt","w+")
f.write("In the beginning.\nThere was light.\nIt is a beautiful day outside.\nThere was light.\nIce cream is a delicious treat on a hot day.\nInvest in yourself, it pays the best interest.")
f.seek(0)
data=f.readlines()
for i in data:
    if len(i.split())>5:
        print(i)
f.close()