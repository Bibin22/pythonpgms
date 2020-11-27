class tutorial:
    def __init__(self):
        self.name = "bibin"
        self.age = 12

    def update(self):
        self.age = 19
        # print(self.age)

    def compare(t1, t2):
        if t1.age == t2.age:

            return True
        else:

            return False


t1 = tutorial()
t2 = tutorial()
t2.age = 23
if t1.compare(t2):
    print("They Are Same")
else:
    print("They are not same")
