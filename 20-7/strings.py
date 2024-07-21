# strings
n="a"
print(n)
n+"b"
print(n)

# strings are immutable
n="a"
print(n)
n=n+"b"
print(n[1])

# slicing in string
name="I am a java trainer"
print(name)
print("name[2:4]",name[2:4])
print("name[5:9]",name[5:9])
print("name[:15]",name[:15])
print("name[2:]",name[2:])
print("name[:]",name[:])
print("name[0:17:3]",name[0:17:3])
print("name[::]",name[::])
print("name[::-1]",name[::-1])


str="rahul"
del str[1]

# is operator
x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is z)
print(x is y)

# capitalize() method
str="the sky"
print(str)
s=str.capitalize()
print(s)

# center()- method aligns strings to the center by filling paddings left and right to the string. This method takes two agruements, first is the width and second is fillchar which is optional. The fillchar is a character which is used to fill left and right padding of the string.
s="Rahul"
print(s)
s1=s.center(15,"*")
print(s1)

# count(<element/substring>,[<start index>],[<end index>])-counts the specified substring in the given string
s="the sky is blue"
print("count:",s.count("s"))

# find(<substring>,[<start index>],[<end task>])-returns index of specified substring
s="welcome to the python class"
s1=s.find("t")
print(s1)

# index(<substring>,[<start index>],[<end index>])-returns index of substring
s="welcome to the python class"
s1=s.index("th",19,21)
print(s1)

# isalnum()-check if string is alphanumeric or not.
# isalpha()-check if string is complete alphabet or not
# lstrip()-removes character from left
# rstrip()-removes character from right
# strip()- removes character from both ends of the string
s="welcome12345"
print(s.isalpha())
print(s.isalnum())
print(s.isdigit())
s="------welcomee------"
print(s.rstrip("-"))
print(s.lstrip("-"))
print(s.strip("-"))


# replace(<old string>,<new string>)
s="java is programming language"
print(s.replace("java","c"))


# swapcase()
s="This is Sky"
print(s.swapcase())

