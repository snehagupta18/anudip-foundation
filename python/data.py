
"""
# ***DAY:1***(09/07/2024)

Selection Statements
"""

#Ques: To display the input time (in sec) into Hour:Minute:Second

time= int(input("enter time in seconds "))
if ((time>=0)):
    hour=0
    min=0
    #conversion of second in hour
    if(time>=3600):
      hour=time//3600
      time=time%3600
    #conversion of second in minute
    if(time>=60):
      min=time//60
      time=time%60
    print(hour,min,time)
else:
    print("time must be positive")

"""finding the greatest number Between two"""

num1=int(input("enter 1st number "))
num2=int(input("enter 2nd number "))

if num1 > num2:
    greatest = num1
else:
    if num2 > num1:
        greatest = num2
    else:
        greatest = "Both numbers are equal"

print("The greatest number is:", greatest)

"""# **DAY:2**(10/07/2024)




"""

#Ques: Given the Cost Price(CP) and Selling Price(SP) of a product. The task is to Calculate the Profit or Loss

cp=float(input("enter cost price (in Rs):  " ))
sp=float(input("enter selling price (in Rs): "))
if(cp<0 ):
    print("invalid cost price")
elif(sp<0):
    print("invalid selling price")
else:
    if(cp>sp):
      print("loss: Rs", (cp-sp))
    elif(cp<sp):
      print("profit: Rs", (sp-cp))
    else:
      print("no profit no loss")

# **DAY:3(11/07/2024)**


#sum of given list

li=[80,90,30,20,70,80,39,87]
sum=0
for x in li:
  sum=sum+x
print(sum)

#The numbers between 10 to 500 dividible by both 10 and 7
for x in range(10,500):
    if(x%7==0 and x%10==0):
        print("The numbers between 10 to 500 dividible by both 10 and 7 are: ",x)

#count the numbers between 100 to 1000 which is even and divisible by 3

count=0
for x in range(100,1000):
  if(x%2==0 and x%3==0):
      print(x, end=",")
      count=count+1
print("\nThe number of numbers between 100 to 1000 which is even and divisible by 3 are: ",count)


# **DAY:4(12/07/2024)**




#**LIST:**


list=[1,2,3,4,"Hello"]
print("Display the list with formatting: ",list)
print("Display the list without formatting:")
print(*list)
print("---Display the list by access member using for loop(ELEMENT BY ELEMENT): ---")
for x in list:
  print(x)





list=[1,2,3,4,5,"hello","World",6,7]
print("Fetching 3rd Element: ")
print(list[2])
print("fetching 4th element from last:")
print(list[-4])
print("Fetching elements from 3rd to 10th position:")
print(list[2:10])
print("Fetching alternate elements from 3rd to 10th position:")
print(list[2:10:2])




#create a list of 20 numbers and print the number in backward direction using forward indexing
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,15,18,19,20]
x=len(list)-1
for i in range(x,-1,-1):
  print(list[i],end=',')




#Ques: Find the method to insert all the element of another sequence datatype at particular index in the list. But all the element must be inserted one by one.
list1=[1,2,3,4,8,9,10]
list2=[5,6,7]
list1.insert(-3,5)
print(list1)

        


#Ques: Find the method to insert all the element of another sequence datatype at particular index in the list. But all the element must be inserted one by one.
list1=[1,2,3,4,8,9,10]
list2=[5,6,7]
index=int(input("Enter the index where you want to insert the list2: "))
if(index<len(list1)):
  a=list1[0:index]
  b=list1[index::]
  a.extend(list2)
  list1.clear()
  list1=a+b
  print("Updateed list will be: ",list1)
else:
  print("Entered index",index,"is out of range")

#Ques: Find the method to insert all the element of another sequence datatype at particular index in the list. But all the element must be inserted one by one.
list1=[1,2,3,4,8,9,10]
list2=[5,6,7]
index=int(input("enter the index where you want to insert the list2: "))
if(index>=0 and index<len(list1)):
  for i in range(len(list2)):
     list1.insert(index+i,list2[i])
  print("Updated list will be: ",list1)
elif(index<0 and index>=-len(list1)):
  for i in range(len(list2)):
     list1.insert(index,list2[i])
  print("Updated list will be: ",list1)
else:
  print("Entered index",index,"is out of range")

"""# **DAY:5**

#**Tabulate module**
* The Tabulate library or Module is used to Display the Data in the form of Row and Column.


"""

#tabulate modeule in python is used to convert the data in tabular form, In tabulate module tabulate function is used here in that question
#Using LIST
from tabulate import tabulate

# Data from the spreadsheet
data = [
    ["std101", "Ashish Kumar", "10th", 15, 67, 89, 87, 89, 90, 422],
    ["std102", "Abhishek Kumar", "10th", 15, 34, 45, 78, 45, 31, 233],
    ["std103", "Aman", "10th", 15, 56, 56, 78, 78, 45, 313],
    ["std104", "Rahul", "10th", 15, 78, 67, 89, 89, 78, 402],
    ["std105", "Ruby", "10th", 13, 89, 56, 45, 45, 67, 302],
    ["std106", "Suman", "10th", 13, 67, 67, 67, 67, 67, 335],
    ["std107", "Saurabh", "10th", 15, 45, 23, 45, 78, 67, 258],
    ["std108", "Sumit", "10th", 15, 89, 90, 89, 90, 45, 403],
    ["std109", "Kamlesh", "10th", 15, 78, 45, 78, 78, 78, 337],
    ["std110", "Rohan", "10th", 15, 12, 24, 45, 56, 34, 171]
]

# Define the headers
headers = ["stdid", "stdname", "standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]

# Print the table
print(tabulate(data, headers=headers, tablefmt="grid"))

# Define the index for English marks
english_index = 5

# Find and print the names of students with English marks greater than 50 using a for loop
print("Students with English marks greater than 70:")
for row in data:
    if row[english_index] > 50:
        print(row[1])

# Extract student name, age, and Maths score
relevant_data = [(row[1], row[3], row[6]) for row in data]

# Sort the data by Maths score in descending order
sorted_data = sorted(relevant_data, key=lambda x: x[2], reverse=True)

# Select the top four students
top_four = sorted_data[:4]

# Print the top four students' names and ages
for student in top_four:
    print(f"Student Name: {student[0]}, Age: {student[1]}")

# Extract student id,name, age, and computer score
relevant_data = [(row[0], row[1],row[3], row[8]) for row in data]

# Sort the data by computer score in descending order
sorted_data = sorted(relevant_data, key=lambda x: x[3], reverse=True)

# Select the bottom three students
bottom_three = sorted_data[-3::]

# Print the bottom three students id, names and ages
for student in bottom_three:
    print(f"Student Id: { student[0]},Student Name: {student[1]}, Age: {student[2]}")





#**DELETION IN DICTIONARY**


student_data={'stdid':'std101','stdname': 'Ashish Kumar','standard': '10th','age': 15,'hindi':67,'English':89}
#To display the dictionary
print(student_data)
#delete element having key as hindi
student_data.pop('hindi')
#To delete the last item in dictionary
student_data.popitem()
print(student_data)
#to return the keys of all the element in List
element_keys=student_data.keys()
print(element_keys)
#To return the values of all the element in List of a Dictionary
element_values=student_data.values()
print(element_values)
#To return the a list of items
dict_items=student_data.items()
print(dict_items)
#To find all the value of all the element
for data in student_data.values():
  print(data)
print("------------*----------------*------------------*----------------")
x= student_data.get('maths')
print(x)
print('------------------*-------------------*---------------*------------')
# Using update()
dict1={'name':'Amit','Age':15,'standard':'10th'}
print(dict1)
dict2={'hindi':67,'Age':16,'standard':"12th",'English':67}
print((dict2))
# inserting all the element of the dict2 into dict1
dict1.update(dict2)
print(dict1)
print('------------------*-------------------*---------------*------------')
#Using fromkeys()
x=dict1.fromkeys('english',16)
print(x)
y=dict1.fromkeys(dict1.keys(),dict1.values())
print(y)
z=dict1.fromkeys(dict1.keys(),16)
print(z)
print("-------------------*-----------------*----------------*----------------")
#To find the no. of element of a dictionary
print(len(dict1))





from tabulate import tabulate
# Using DICTIONARY
# Data of the Student from Excel
data = [
    {"stdid": "std101", "stdname": "Ashish Kumar", "standard": "10th", "Age": 15, "Hindi": 67, "English": 89, "Maths": 87, "Science": 89, "Computer": 90, "Total": 422},
    {"stdid": "std102", "stdname": "Abhishek Kumar", "standard": "10th", "Age": 15, "Hindi": 34, "English": 45, "Maths": 78, "Science": 45, "Computer": 31, "Total": 233},
    {"stdid": "std103", "stdname": "Aman", "standard": "10th", "Age": 15, "Hindi": 56, "English": 56, "Maths": 78, "Science": 78, "Computer": 45, "Total": 313},
    {"stdid": "std104", "stdname": "Rahul", "standard": "10th", "Age": 15, "Hindi": 78, "English": 67, "Maths": 89, "Science": 89, "Computer": 78, "Total": 402},
    {"stdid": "std105", "stdname": "Ruby", "standard": "10th", "Age": 13, "Hindi": 89, "English": 56, "Maths": 45, "Science": 45, "Computer": 67, "Total": 302},
    {"stdid": "std106", "stdname": "Suman", "standard": "10th", "Age": 13, "Hindi": 67, "English": 67, "Maths": 67, "Science": 67, "Computer": 67, "Total": 335},
    {"stdid": "std107", "stdname": "Saurabh", "standard": "10th", "Age": 15, "Hindi": 45, "English": 23, "Maths": 45, "Science": 78, "Computer": 67, "Total": 258},
    {"stdid": "std108", "stdname": "Sumit", "standard": "10th", "Age": 15, "Hindi": 89, "English": 90, "Maths": 89, "Science": 90, "Computer": 45, "Total": 403},
    {"stdid": "std109", "stdname": "Kamlesh", "standard": "10th", "Age": 15, "Hindi": 78, "English": 45, "Maths": 78, "Science": 78, "Computer": 78, "Total": 337},
    {"stdid": "std110", "stdname": "Rohan", "standard": "10th", "Age": 15, "Hindi": 12, "English": 24, "Maths": 45, "Science": 56, "Computer": 34, "Total": 171}
]
# To print the data in tabular form
print(tabulate(data, headers="keys", tablefmt="grid"))
# Initialize an empty list to store names of students
filtered_students = []
# To check if the student's English marks is greater than 50
for student in data:
    if student["English"] > 50:
        filtered_students.append(student["stdname"])
# Print the names of students
print("Students whose marks in English are greater than 50:")
for name in filtered_students:
    print(name)

print("------------------*------------------*-----------------*------------------")
print("Name and Age of a student who are top four scorer in Maths:")
# Sort data based on Maths scores in descending order
sorted_data = sorted(data, key=lambda x: x["Maths"], reverse=True)
top_four = sorted_data[0:4]
# Prepare table data that contain the name and age of top four scorer of Maths
table_data = [[student["stdname"], student["Age"]] for student in top_four]
# Display the table_data in tabular form
print(tabulate(table_data, headers=["Student Name", "Age"], tablefmt="grid"))

print("------------------*------------------*-----------------*------------------")
print("Name, Id and Age of student who are bottom three scorer in Computer:")
# Sort data based on Computer scores in ascending order
sorted_data = sorted(data, key=lambda x: x["Computer"])
bottom_three = sorted_data[:3]

#Prepare table data that contain the Name ,Id and Age of bottom three scorer in Computer
table_data = [[student["stdname"], student["stdid"], student["Age"]] for student in bottom_three]
# Display the table_data in tabular form
print(tabulate(table_data, headers=["Student Name", "Student ID", "Age"], tablefmt="grid"))