class details:
    year = 2020


    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place


    def addage(self):
        self.age = self.age + 1


    def disp(self):
        print("----------------------------------------------------------------------------------------------------------")
        print("Year",details.year)
        print("Name :", self.name)
        print("age", self.age)
        print("place:", self.place)


    @classmethod
    def add_year(cls):
        cls.year = cls.year+1


name = input("enter a name")
age = int(input("enter age"))
place = input("enter place")


x = details(name,age,place)
x.disp()

details.year = details.year+1
x.addage()
print(". . . .. . . . . . . . . . . . . . . . .  .A F T E R 1 Y E A R. . . . . .  . . . . .  . . . . . . .  . . . . . .  . ")
x.disp()


details.add_year()
x.addage()
print(". . . .. . . . . . . . . . . . . . . . .  .A F T E R 2 Y E A R. . . . . .  . . . . .  . . . . . . .  . . . . . .  . ")
x.disp()
