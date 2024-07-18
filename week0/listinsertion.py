l=[20,30,40,50]
print("after append")
l.append(int(input("enter a number")))
print(l)
print("after extend")
l.extend(eval(input("enter list: ")))
print(l)