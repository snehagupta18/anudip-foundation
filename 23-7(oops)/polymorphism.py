# python does not support method over loading
# Polymorphism- Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.

def setdata(id,name):
    print("id,name")
    
def setdata(id,name,age):
    print("id,name,age")

# setdata(101,"abc") #ERROR    


def sum(a,b,c=0):
    print(a+b+c)
sum(10,20,30)
sum(10,20)