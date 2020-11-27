class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 =m2

    def display(self):
        total = self.m1 + self.m2
        print("Mark 1 =", self.m1)
        print("Mark2 =", self.m2)
        print("Total =", total)

    def __add__(s1, s2):
        m1 = s1.m1 + s2.m1
        m2 = s1.m2 + s2.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(s1, s2):
        r1 = s1.m1 + s1.m2
        r2 = s2.m1 + s2.m2
        if r1 > r2 :
            return True
        else:
            return False






mark1 = int(input("Enter Mark1"))
mark2 = int(input("Enter Mark2"))

mrk1 = int(input("Enter Mark1"))
mrk2 = int(input("Enter Mark2"))



s1 = Student(mark1, mark2)
s1.display()
s2 = Student(mrk1, mrk2)
s2.display()


s3 = s1 + s2
print('s3.m1 =', s3.m1)
print('s3.m2 = ', s3.m2)
print()


if s1 > s2 :
    print("S1 WINSSSSSSSSSS")
else:
    print("S2 Winssssss")
