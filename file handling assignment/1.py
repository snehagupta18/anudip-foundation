# 1. program to count occurrence of the word "India" in the text file india.txt

f=open("file handling assignment/india.txt","w")
f.write("India is a land of diverse cultures and rich heritage, boasts a captivating blend of ancient traditions and modern aspirations.\nIndia is a vibrant tapestry of languages, religions, and landscapes, continues to mesmerize the world with its unique charm.")
f.close()
f=open("file handling assignment/india.txt","r")
data=f.readlines()
c=0
for i in data:
    list=i.split()
    for j in list:
        if j=="India":
            c+=1
# print(data)
print("occurence=",c)
f.close()