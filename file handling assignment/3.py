# 3- to count number of vowels and consonants

f=open("file handling assignment/Myfile.txt","w+")
f.write("The quick brown fox jumps over the lazy dog.\nSky is blue.\nTime flies when you're having fun.")
f.seek(0)
data=f.read()
vowel,consonant=0,0
for i in data:
    if i.lower() in "aeiou":
        vowel+=1
    elif i.lower() in "bcdfghjklmnpqrstvwxyz":
        consonant+=1
print("vowels=",vowel)
print("consonants=",consonant)
f.close()
    