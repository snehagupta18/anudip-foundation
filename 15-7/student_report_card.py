import pandas as pd
student=[['std101','ashish kumar','10th',15,67,89,87,89,90,422],
         ['std102','abhishek kumar','10th',14,85,45,48,90,45,313],
         ['std103','aman','10th',15,23,56,78,78,67,302],
         ['std104','rahul','10th',14,45,76,45,45,56,258],
         ['std105','ruby','10th',13,89,67,89,93,65,403],
         ['std106','suman','10th',13,90,46,67,67,67,337],
         ['std107','saurabh','10th',15,45,23,34,45,34,181],
         ['std108','sumit','10th',14,23,45,67,78,90,345],
         ['std109','kamlesh','10th',15,45,56,78,99,67,345],
         ['std110','rohan','10th',15,34,12,24,45,56,171]]
columns=['stdid','stdname','standard','age','hindi','english','maths','science','computer','total']
df=pd.DataFrame(data=student,columns=columns)
print(df)
print()

#names of students who have marks in english greater than 50
print("-----students with marks>50 in english------")
for row in student:
    if row[5]>50:
        print(row[1])
print()

#display name and age of top 4 scorers of maths
print('-------name and age of top 4 scorers of maths------')
score=sorted(student, key=lambda row: row[6], reverse=True)
print('name','age')
print(score[0][1],score[0][3])
print(score[1][1],score[0][3])
print(score[2][1],score[0][3])
print(score[3][1],score[0][3])
print()

#display name,id,age of students who are bottom three scorer in computers
print('-------name,id and age of bottom 3 scorers of computers------')
score=sorted(student, key=lambda row: row[8])
print('name','id','age')
print(score[0][1],score[0][0],score[0][3])
print(score[1][1],score[1][0],score[0][3])
print(score[2][1],score[2][0],score[0][3])


from tabulate import tabulate
student_table=tabulate(student,headers=columns,tablefmt="grid")
print(student_table)
