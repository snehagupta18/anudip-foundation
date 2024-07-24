class A: #parent class
    def show(self):
        print("This is show method")
        
class B(A): #B inherits parent class A
    def demo(self):
        print("demo method")
class C(A): #C inherits parent class A
    pass
class D(B,C): #D inherits parent class B,C
    pass

obj=C()
obj.show()
obj.demo() #error