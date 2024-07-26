# reshape()-is used to reshape an array
# .shape- is used to find the shaspe of the array

import numpy as np
a=np.array([1,2,3,4,5,50,43,2])
print(a)
b=a.reshape(4,2)
print(b)
c=a.reshape(-1,4) #-1 is used for auto adjustment
print(c)

print("element=",b[2][1])
