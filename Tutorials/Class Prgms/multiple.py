class First:
    def details(self, name, rno, std):
        self.name = name
        self.rno = rno
        self.std = std


class Second:
    def subjects(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3


class Third(First, Second):
    def marks(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        total = self.m1 + self.m2 + self.m3
        print("Student Name :", self.name)
        print("Student Roll Number : ", self.rno)
        print("Sutdent Class", self.std)
        print("Subject 1:", self.sub1)
        print("Subject 2:", self.sub2)
        print("Subject 3:", self.sub3)
        print("Mark of ", self.sub1, "is ", self.m1)
        print("Mark of ", self.sub2, "is ", self.m2)
        print("Mark of ", self.sub3, "is ", self.m3)
        print(self.name, "Got Total", total, "Marks")


name = input("Enter Student Name")
rno = int(input("Enter Roll NUmber "))
std = input("Enter class name ")

sub1 = input("Enter Subject 1:")
sub2 = input("Enter Subject 2:")
sub3 = input("Enter Subject 3:")

m1 = int(input("Enter Mark for Subject 1"))
m2 = int(input("Enter Mark for Subject 2"))
m3 = int(input("Enter Mark for Subject 3"))


ob = Third()
ob.details(name, rno, std)
ob.subjects(sub1, sub2, sub3)
ob.marks(m1, m2, m3)
ob.display()

