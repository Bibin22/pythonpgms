class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def display(self):
        print("Name :", self.name)
        print("Age", self.age)
        print("Height", self.height)


person1 = Person("Bibin", 12, 145)
person1.display()
person2 = Person("AAAA", 23, 156)
person2.display()
print(id(person1))
print(id(person2))
