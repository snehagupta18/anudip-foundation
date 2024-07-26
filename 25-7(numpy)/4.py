import numpy as n
n.random.seed(122)
mat=n.random.randint(1,21,9).reshape(3,3)
print(mat)
print(n.sum(mat))
print(n.cumsum(mat)) #cumulative sum
print(n.min(mat))
print(n.max(mat))
print("------------------")
print(n.sum(mat,axis=1)) #axis=1->row
print(n.min(mat,axis=1))
print(n.max(mat,axis=1))
print(n.cumsum(mat,axis=1))

# shuffle-is used to shuffle the values of the array
import numpy as np
np.random.seed(122)
mat=np.random.randint(1,21,10)
print(mat)
print()
np.random.shuffle(mat)
print(mat)
print()
print(np.unique(mat,return_index=True,return_counts=True))
print()
print(np.unique(mat).size)
