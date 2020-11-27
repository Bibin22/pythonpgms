class Pycharm:
    def execute(self):
        print("Compiling")
        print("Run")
class Mycode:
    def execute(self):
        print("Spell Check")
        print("Error")

class Laptop:
    def code(self,ide):
        ide.execute()
ide = Pycharm() #ivide objectinu ide ennu thane kodukanam ennila vere peru koduthalum work aakum
my = Mycode()
lap = Laptop()
lap.code(ide)
#lap.code(my)
