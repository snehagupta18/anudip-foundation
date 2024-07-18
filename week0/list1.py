#create a list of the numbers and display the elements in backward direction usind forward index.

l=[1,2,3,4,5]
n=len(l)
# for i in range(0,n):
#     print(l[n-i-1])


# i=0
# while(i<n):
#     print(l[n-i-1])
#     i+=1

for i in range(n-1,-1,-1):
    print(l[i],end=' ')