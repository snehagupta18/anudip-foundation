# difference between view and copy
# copy()-forms a complete new array
# view()-allocates the original array

import numpy as np
arr = np. array ([1, 2, 3, 4, 5, 6, 7])
sarr=arr [1:5]
print (arr)
print (sarr)
sarr [2]=100
print (arr)
print (sarr)

print("copy")
arr=np.array([1,2,3,4,5])
arr2=arr.copy()
print(arr)
print(arr2)
print("------------")
arr[0]=42
print(arr)
print(arr2)

print("view")
arr=np.array([1,2,3,4,5])
arr2=arr.view()
print(arr)
print(arr2)
print("------------")
arr[0]=42
print(arr)
print(arr2)