class Baseclass:
    def __init__(self):
        print("Base Class ___init__")
    def function(self):
        print("Base Class Function")
class Subclass(Baseclass):
    def __init__(self):
        print("Sub Class __init__")
    def function(self):
        print("Sub Class Function")
x = Subclass()
#x.__init__()
x.function()
print(""" If base class and sub class has same constructor name and ( or ) function name 
only the subclass funtions or counstructor will be output check overriding2.py  """)