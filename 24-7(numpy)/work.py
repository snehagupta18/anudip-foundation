# 1-dim array-vector
# 2-dim array-matrix
# 3-dim array-tensor

import numpy as np
d=np.array([10,20,30,40])
a=np.array(42)
# print(a)
b=np.array([[10,20,30,40],[10,20,30,40]])
c=np.array([[10,20,30,40],[10,20,30,40],[10,20,30,40]])

# to check dimension on array
print("a dimension=",a.ndim)
print("b dimension=",b.ndim)
print("c dimension=",c.ndim)
print("d dimension=",d.ndim)

print(d[1])

