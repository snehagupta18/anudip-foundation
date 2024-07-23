# 2- to count and display the lines starting with "T" in text file story.txt.

f=open("file handling assignment/story.txt","w+")
f.write("The quick brown fox jumps over the lazy dog.\nSky is blue.\nTime flies when you're having fun.")
f.seek(0)
c=0
data=f.readlines()
for i in data:
    if i[0]=='T':
        c+=1
        print(i)
print("count=",c)
f.close()