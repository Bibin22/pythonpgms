car = ['bugati','audi','bmw','benz','cheverlot','ford', 'bently', 'tezla', 'volvo','ferrari']
print(car)

car.append('lamborgini')
car.insert(3, 'toyota')
car.extend(['innova', 'cooper', 'lexexus'])
print(car)
car.sort()
print(car)
car.remove('innova')
print(car)
car.pop()
print(car)
car.pop(7)
print(car)
car.reverse()
print(car)
car2 = car.copy()
print('car2 =', car2)