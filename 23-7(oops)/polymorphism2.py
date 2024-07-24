class bird:
    def intro(self):
        print("there are many type of bird")
    def flight(self):
        print("most birds can fly, but some can not")
        
class sparrow(bird):
    def flight(self):
        print("sparrow-i can fly")
class ostrich(bird):
    def flight(self):
        print("ostrich-i can not fly")
 
b=bird()
b.intro()
b.flight()
a=sparrow()
a.flight()        
s=ostrich()
s.flight()
