class Details:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
    def display(self):
        print("Name:", self.name)
        print("RollNo:", self.rno)
class Std:
    def __init__(self, strd):
        self.strd = strd
    def display(self):
        print("Class", self.strd)

class Output:
    def students(self, st):
        st.display()


name = input(" enter a name")
rno = int(input("enter roll no"))
strd = input("Enter Class")


de = Details(name, rno)
sd = Std(strd)
out = Output()
out.students(de)
out.students(sd)
