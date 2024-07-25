# basic numpy functions

import numpy as np
a=np.zeros((5,),dtype=int) #withput order
b=np.ones((5,2),dtype=int) #with shape
c=np.zeros(7)+10 #withput dtype and order
print(a)
print(b)
print(c)

arr4=np.eye(3)
print(arr4)

arr5=np.eye(3,4)
print(arr5)

arr6=np.diag([1,2,3,4])
print(arr6)
print("dimension=",arr6.ndim)
print("shape=",arr6.shape)
