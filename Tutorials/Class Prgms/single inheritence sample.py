class details:
    def myname(self, name):
        self.name = name
    def welcome(self):
        print("WELCOME TO OOTY NICE TO MEET YOU")
class name(details):
    def display(self):
        print("hello", self.name)
x = name()
x.myname("BIBIN")
x.display()
x.welcome()