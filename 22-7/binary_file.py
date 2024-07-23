# pickle module is used to read and write data in binary format
# dump(<data>,<file object>)- used to write data in binary format
# load(<file object>)- used to read a binary file

import pickle
f=open("22-7/anudip.dat","wb")
l=[10,20,30,40]
pickle.dump(l,f)
f.close()

f=open("22-7/anudip.dat","rb")
# l=[10,20,30,40]
data=pickle.load(f)
print(data)
f.close()
