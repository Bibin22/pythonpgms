class Student:
    school = "ICET" #Class Variable
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        avrg = (self.m1 + self.m2 + self.m3) / 3
        print(avrg)
        #return(self.m1 + self.m2 + self.m3) / 3
    @classmethod
    def inf(cls):
        return cls.school
    @staticmethod
    def static():
        print("This is Static Method")



s1 = Student(12, 23, 45)
s1.avg()
print(Student.inf())
s1.static()
