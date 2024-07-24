# oops


class student:
    name="xyz"
    age=0
    def study(self):
        print("study 3 hours",self.name)
        # self.sleep()
    def sleep(self):
        print("sleep 1 hour")
        self.study()

obj=student()
obj.study()
# obj.sleep()