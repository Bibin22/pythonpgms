class name:
    def __init__(self, fname):
        self.fname = fname


    def __add__(fst, scnd):
        full = fst.fname +" " + scnd.fname
        return full

f = input("Enter  Name")
n = input(" Enter Second Name")
fst = name(f)
scnd = name(n)
full = fst + scnd
print(full)





