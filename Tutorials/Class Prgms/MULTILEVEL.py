class First:
    def name(self, name):
        self.name = name

class Second(First):
    def age(self, age):
        self.age = age
class Third(Second):
    def display(self):
        print("Name", self.name)
        print("Age", self.age)

name = input("enter name")
age = int(input("Enter age"))
ob = Third()
ob.name(name)
ob.age(age)
ob.display()