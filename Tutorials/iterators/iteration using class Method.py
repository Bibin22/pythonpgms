class Topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            #print("val1", val)
            self.num += 1
            #print("self.num =", self.num)
           #print("val2", val)
            return val
        else:
            raise StopIteration


values = Topten()
for i in values:
    print(i)

print("For clear some doubt un command those statements")
