# c=0
# for x in range(101,1000):
#     if(x%2==0 and x%3==0):
#         c+=1
#         print(x,end=' ')
# print(c)

x=100
c=0
while(x<1000):
    if(x%2==0 and x%3==0):
        c+=1
        print(x,end=' ')
    x+=1
print("count=",c)