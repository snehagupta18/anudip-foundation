# writer- to create writer object
# writerow-to write single row
# writerows-to write multiple rows
# reader- to create reader object


import csv
f=open("22-7/anudip.csv",'w',newline='')
wo=csv.writer(f)
data=[['a','b','c','d'],[10,20,30,40],[20,30,40,50],[40,50,30,20]]
wo.writerows(data)
f.close()

f=open("22-7/anudip.csv",'r')
r=csv.reader(f)
data=list(r)
for i in data:
    print(i)
# print(data)
f.close()
