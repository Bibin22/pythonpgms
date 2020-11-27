class Student:
    def sum(self, a = None, b = None, c = None):
        if a!= None and b!= None and c!=None:
            s = a + b + c

        elif a!= None and b!= None:
            s = a + b

        else:
            s = a
        print("sum =", s)

s1 = Student()
s1.sum(12, 45, 67)
s1.sum(34, 67)
s1.sum(56)





