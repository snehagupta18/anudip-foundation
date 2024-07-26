import numpy as np
a=np.arange(1,15) #generate numbers in sequence
print(a)
print(a[a%2==0])
print(a[a%2!=0])
print(a[a>8])
a[a%2==0]=0
print(a)
