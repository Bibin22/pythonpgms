class Car:
    wheels = 4
    def __init__(self):
        self.car ="BMW"
        self.mil =12

c1 = Car()
c2 = Car()
c1.car = "Audi"
c1.mil = 19
Car.wheels = 17
print(c1.car, c1.mil, Car.wheels)
print(c2.car, c2.mil, Car.wheels)