# _-protected
# __-private

class A:
    __name="abc"
    
class B(A):
    def show(self):
        print("this is show method",self.name)
        
obj=B()
obj.show()