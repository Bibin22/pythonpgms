class Baseclass:
    def __init__(self):
        print("Base Class ___init__")
    def function(self,name):
        self.name = name
        print("Base class name", self.name)
        #print("Base Class Function")
class Subclass(Baseclass):
    def __init__(self):
       super().__init__()          #Constructor Over Riding Caliing Metod 1
       #Baseclass.__init__(self)   #Constructor Over Riding Caliing Metod 2
    print("Sub Class __init__")
    def function(self,name,age):
       # Baseclass.function(self,name) #Function Over Riding Calling Method 1
        super().function(name)         #Function Over Riding Calling Method 1
        self.age = age

        print("Sub Class Age :", self.age)
x = Subclass()
#x.__init__()
x.function("bibin", 12)
print("""  here we can solve the problem of overriding by using super().funtionname or Classname.functionname (in this program class Name is 'BaseClass'  """)