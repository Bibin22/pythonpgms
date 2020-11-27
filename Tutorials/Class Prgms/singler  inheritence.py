class student:
    def read(self, name, rno, clas):
        self.name = name
        self.rno = rno
        self.clas = clas


class mark(student):
    def readmark(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def writemark(self):
        total = self.m1 + self.m2 + self.m3
        print("Name:", self.name)
        print("Roll.No:", self.rno)
        print("Class", self.clas)
        print("Total Marks", total)


name = input("Enter Name")
rno = int(input("Enter Roll No"))
clas = input("Enter Class")
m1 = int(input("Enter Mark1"))
m2 = int(input(" Enter Mark2"))
m3 = int(input(" Enter Mark2"))
x = mark()
x.read(name, rno, clas)
x.readmark(m1, m2, m3)

x.writemark()
