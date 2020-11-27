class names:
    def read(self,nme):
        self.name = nme
    def write(self):
        print(self.name)
name = "bibin"
x = names()
y = names()
x.read(name)
y.read("bibin joy")
x.write()
y.write()