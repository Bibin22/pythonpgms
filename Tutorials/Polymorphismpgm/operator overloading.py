class operator:
    def setname(self,name):
        self.name = name
    def __add__(self, other):
        name =self.name + " " + other.name   #here self.name = "bibin" and other.name = "joy"
        return name
firstname = operator()
secondname = operator()
firstname.setname("bibin")
secondname.setname("joy")
fullname = firstname + secondname
print(fullname)