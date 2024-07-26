import numpy as np
ar=np.array([1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33])
slicing=ar[4:9]
print("new slicing:",slicing)
print("new array",ar)
print(type(slicing))
print(type(ar))
slicing[:]=0
print("old slicing",slicing)
print("old array",ar)