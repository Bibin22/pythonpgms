class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.processor ='i3'
        def show1(self):
            print(self.brand, self.processor)


s1 = Student('bibin', 12)
lap = Student.Laptop()
lap.show1()
s1.show()
